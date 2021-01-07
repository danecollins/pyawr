from typing import List, Iterable, Any, Tuple
import win32com.client
import pyawr.mwoffice as mwo
import os
import numpy as np
import pandas as pd


def connect(version: str=None, clsid: str=None) -> Tuple[Any, Any]:
    """ Connects to AWRDE and returns the entry point and definition of the constants

        :param version: if this is specified that version will be used
        :param clsid: if this is specified then the connection will be to the specific instance
        :return: a tuple of the connection and the constants for awrde
    """

    # registered in Computer\HKEY_CLASSES_ROOT\AWR
    # and HKEY_CLASSES_ROOT\CLISD\{...} for the executable

    if clsid:
        if clsid[0] == '{' and clsid[-1] == '}':
            awrde = win32com.client.Dispatch(clsid)
        else:
            raise ValueError('CLSID string but start and end with braces "{}" - got {}'.format(clsid))
    else:
        appname = 'AWR.MWOffice'
        if version:
            appname += '.' + version
        awrde = win32com.client.Dispatch(appname)
    return awrde


def open_example(awrde: Any, s: str) -> None:
    """ Open a file from the example directory """
    p = awrde.Directories(8).ValueAsString
    awrde.Open(os.path.join(p, s))


def vbrange(i: int) -> range:
    """ returns a 1 based range for visual basic iterators """
    return range(1, i + 1)


def as_list(object: Any) -> List[Any]:
    """ returns iterator objects as a list """
    return [object(i) for i in vbrange(object.Count)]


def meas_from_graph(awrde: Any, name: str) -> List[Any]:
    """ Given the name of the graph return a list of measurements """
    g = awrde.Project.Graphs(name)
    return list(g.Measurements)


class AwrMeas:
    name = None  # type: str
    source = None  # type: str
    data_type = None  # type: str
    plot_dim = None  # type: int
    x_units = None  # type: str
    y_units = None  # type:str
    df = None  # type: Any

    def meas_to_df(self) -> Any:
        """ Given a measurement return a dataframe of the data """
        d = []  # start by creating a list of dictionary
        m = self.measurement
        for trace in vbrange(m.TraceCount):
            info = {}
            info['source'] = self.source
            info['name'] = self.name
            for labels in vbrange(m.SweepLabels(trace).Count):
                n = m.SweepLabels(trace).Item(labels).Name
                v = m.SweepLabels(trace).Item(labels).Value
                ut = mwo.mwUnitType(m.SweepLabels(trace).Item(labels).UnitType)._name_
                #ut = mwUnitType(m.SweepLabels(trace).Item(labels).UnitType)
                info[n] = v
                info[n + '_unit'] = ut
            points = m.TraceValues(trace)
            for (x, y) in points:
                tmp = info.copy()
                tmp['x'] = x
                tmp['y'] = y
                d.append(tmp)
        return pd.DataFrame(d)  # convert to dataframe

    def __init__(self, m: Any) -> None:
        (source, name) = m.Name.split(':')
        self.measurement = m
        self.name = name
        self.source = source
        self.data_type = mwo.mwMeasDataType(m.DataType)._name_
        self.plot_dim = m.PlotDimension
        self.x_units = mwo.mwUnitType(m.UnitType(1))._name_
        self.y_units = mwo.mwUnitType(m.UnitType(2))._name_
        self.df = self.meas_to_df()


    def __str__(self) -> str:
        return "AwrMeas({}:{},type={},dim={},pts={})".format(self.source, self.name,
                                                             self.data_type, self.plot_dim, len(self.df))
