from typing import List, Iterable, Any, Tuple
import win32com.client
import pyawr.mwoffice as mwo
import os
import numpy as np
import pandas as pd


def open_example(awrde: mwo.CMWOffice, s: str) -> None:
    """ Open a file from the example directory """
    p = awrde.Directories(8).ValueAsString
    awrde.Open(os.path.join(p, s))


def vbrange(i: int) -> range:
    """ returns a 1 based range for visual basic iterators """
    return range(1, i + 1)


def as_list(object: Any) -> List[Any]:
    """ returns iterator objects as a list """
    return [object(i) for i in vbrange(object.Count)]


def meas_from_graph(awrde: mwo.CMWOffice, name: str) -> List[Any]:
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
        m = self.measurement
        trace_data = []
        for trace_index in vbrange(m.TraceCount):
            # each trace has a set of swept variable labels, collect those in row dict
            row = {}
            for label in as_list(m.SweepLabels(trace_index)):
                name = label.Name + '(' + mwo.mwUnitType(label.UnitType)._name_ + ')'
                row[name] = label.Value
                
            # now iterate through the trace x/y values and add them
            points = m.TraceValues(trace_index)
            for (x, y) in points:
                tmp = row.copy()
                tmp['x'] = x
                tmp['y'] = y
                trace_data.append(tmp)        
        df = pd.DataFrame.from_records(trace_data)
        return df


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
