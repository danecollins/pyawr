# -*- coding: utf-8 -*-
"""
    This script walk through a measurement that contains sweep variables, converting the multiple
    traces into a single dataframe
"""
import pdb
import pandas as pd
import pyawr.mwoffice as mwo
from pyawr.helpers import vbrange, as_list


awrde = mwo.CMWOffice()

# get one measurement
m = awrde.Project.Graphs('Output Match').Measurements('LPF:DB(|S(2,2)|)')

# get the string and separate the source name measurement name
source, name = m.Name.split(':')
print(f'Measurement name is {name}')
print(f'Measure is on source: {source}')

# The data type is an enumeration, the mwMeasDataType functions lets us map this to a string
data_type = mwo.mwMeasDataType(m.DataType)._name_
print(f'The measurement data type is {data_type}')

print(f'The dimension of the plot is {m.PlotDimension}')
x_units = mwo.mwUnitType(m.UnitType(1))._name_
y_units = mwo.mwUnitType(m.UnitType(2))._name_
print(f'The x units are {x_units} and the y units are {y_units}')

print(f'There are {m.TraceCount} trace(s) for this measurement')

# convert all trace data into a dataframe
trace_data = []
for trace_index in vbrange(m.TraceCount):
    # each trace has a set of swept variable labels, collect those in row dict
    row = {}
    for label in as_list(m.SweepLabels(trace_index)):
        row[label.Name] = label.Value
        
    # now iterate through the trace x/y values and add them
    points = m.TraceValues(trace_index)
    for (x, y) in points:
        tmp = row.copy()
        tmp['x'] = x
        tmp['y'] = y
        trace_data.append(tmp)        
df = pd.DataFrame.from_records(trace_data)
df.head()
    

pdb.set_trace()




    # def __init__(self, m: Any) -> None:
    #     (source, name) = m.Name.split(':')
    #     self.measurement = m
    #     self.name = name
    #     self.source = source
    #     self.data_type = mwo.mwMeasDataType(m.DataType)._name_
    #     self.plot_dim = m.PlotDimension
    #     self.x_units = mwo.mwUnitType(m.UnitType(1))._name_
    #     self.y_units = mwo.mwUnitType(m.UnitType(2))._name_
    #     self.df = self.meas_to_df()

    #         for labels in vbrange(m.SweepLabels(trace).Count):
    #             n = m.SweepLabels(trace).Item(labels).Name
    #             v = m.SweepLabels(trace).Item(labels).Value
    #             ut = mwo.mwUnitType(m.SweepLabels(trace).Item(labels).UnitType)._name_
    #             #ut = mwUnitType(m.SweepLabels(trace).Item(labels).UnitType)
    #             info[n] = v
    #             info[n + '_unit'] = ut
    #         points = m.TraceValues(trace)
    #         for (x, y) in points:
    #             tmp = info.copy()
    #             tmp['x'] = x
    #             tmp['y'] = y
    #             d.append(tmp)