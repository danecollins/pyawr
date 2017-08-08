from typing import Tuple, Iterable, Any
import win32com.client
import os
import numpy as np
import pandas as pd
from cmap import mwUnitType, mwMeasDataType


def connect(version: str=None, clsid: str=None):
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
    return awrde, win32com.client.constants


def open_example(awrde: Any, s: str) -> None:
    """ Open a file from the example directory """
    p = awrde.Directories(8).ValueAsString
    awrde.Open(os.path.join(p, s))


def vbr(i):
    """ returns a 1 based range for visual basic iterators """
    return range(1, i+1)


def as_list(object):
    """ returns iterator objects as a list """
    return [object(i) for i in vbr(object.Count)]


def meas_from_graph(name):
    """ Given the name of the graph return a list of measurements """
    global awrde
    g = awrde.Project.Graphs(name)
    return as_list(g.Measurements)


def meas_to_df(m):
    """ Given a measurement return a dataframe of the data """
    d = []  # start by creating a list of dictionary
    (source, name) = m.Name.split(':')
    for trace in vbr(m.TraceCount):
        info={}
        info['source'] = source
        info['name'] = name
        for labels in vbr(m.SweepLabels(trace).Count):
            n = m.SweepLabels(trace).Item(labels).Name
            v = m.SweepLabels(trace).Item(labels).Value
            ut = mwUnitType(m.SweepLabels(trace).Item(labels).UnitType)
            info[n] = v
            info[n + '_unit'] = ut
        points = m.TraceValues(trace)
        for (x, y) in points:
            tmp = info.copy()
            tmp['x'] = x
            tmp['y'] = y
            d.append(tmp)
    return pd.DataFrame(d)

class AwrTrace:
    def __init__(self, m, index):
        self.sweep_label = m.SweepLabels(index)
        self.data = m.TraceValues(index)

class AwrMeas:
    def __init__(self, m):
        (source, name) = m.Name.split(':')
        self.name = name
        self.source = source
        self.type =  mwMeasDataType(m.DataType)
        self.plot_dim = m.PlotDimension
        self.x_units = mwUnitType(m.UnitType(1))
        self.y_units = mwUnitType(m.UnitType(2))
        self.df = meas_to_df(m)
        
    def __str__(self):
        return "AwrMeas({}:{},type={},dim={},pts={})".format(self.source, self.name,
                       self.type, self.plot_dim, len(self.df))
        
    