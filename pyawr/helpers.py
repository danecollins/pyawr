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


class AwrMeasurement():
    def __init__(self, measurement: mwo.CMeasurement):
        (source, name, simulator) = self.parse_meas_string(measurement.Name)

        self.name = name
        self.source = source  # schematic name for example
        self.simulator = simulator
        self.data_type = mwo.mwMeasDataType(measurement.DataType)._name_
        self.plot_dim = measurement.PlotDimension
        self.x_units = mwo.mwUnitType(measurement.UnitType(1))._name_
        self.y_units = mwo.mwUnitType(measurement.UnitType(2))._name_

    @classmethod
    def parse_meas_string(cls, s: str) -> Tuple[str, str, str]:
        (source, name) = s.split(':')
        if '.' in source:
            (source, simulator) = source.split('.')
        else:
            simulator = ''
        return (source, name, simulator)

class Netlister:
    def __init__(self, awrde: mwo.CMWOffice, schematic: mwo.CSchematic):
        self.awrde = awrde
        self.schematic = schematic
        self.subcircuits = set()
        self.datafiles = set()


    def output_nodes(self, element):
        for i, n in enumerate(element.Nodes, 1):
            pn = n.PortNumber
            nn = n.NodeNumber
            print(f'pin({i})=node({nn}) ', end='')

    def output_parameters(self, element):
        for p in element.Parameters:
            print(f'{p.Name}={p.ValueAsString} ', end='')

    def output_element(self, elem: mwo.CElement):
        awrde = self.awrde
        if 'SUBCKT' in elem.Name:
            # get the name of the subcircuit, will be double quoted so remove them
            subckt_name = elem.Parameters('NET').ValueAsString.replace('"', '')
            # need to determine the type
            if awrde.Project.Schematics.Exists(subckt_name):
                self.output_sch_subcircuit(elem, subckt_name)
            elif awrde.Project.EMStructures.Exists(subckt_name):
                self.output_em_structure(elem, subckt_name)
            elif awrde.Project.EM3DStructures.Exists(subckt_name):
                self.output_em3d_structure(elem, subckt_name)
            elif awrde.Project.DataFiles.Exists(subckt_name):
                self.output_datafile(elem, subckt_name)
            else:
                raise ValueError(f'Cannot find subcircuit named "{subckt_name}"')
        else:
            try:
                (name, _) = elem.Name.split('.')
            except:
                # elements like GND don't have ID's
                name = elem.Name
            print(f'{name} ', end='')
            self.output_nodes(elem)
            self.output_parameters(elem)
            print()


    def output_em_structure(self, elem: mwo.CElement, name: str):
        print(f'EM_Structure ', end='')
        self.output_nodes(elem)
        self.output_parameters(elem)
        print()


    def output_em3d_structure(self, elem: mwo.CElement, name: str):
        print(f'3DEM_Structure ', end='')
        self.output_nodes(elem)
        self.output_parameters(elem)
        print()

    def output_sch_subcircuit(self, elem: mwo.CElement, name: str):
        print(f'Subcircuit ', end='')
        self.output_nodes(elem)
        self.output_parameters(elem)
        self.subcircuits.add(name)

    def output_datafile(self, elem: mwo.CElement, name: str):
        print(f'Datafile ', end='')
        self.output_nodes(elem)
        self.output_parameters(elem)
        self.datafiles.add(name)

    def generate(self):
        for element in self.schematic.Elements:
            self.output_element(element)
        
        # now we have to netlist all the referenced schematics
        while self.subcircuits:
            schematic_name = self.subcircuits.pop()
            # get the schematic by name
            schematic = self.awrde.Project.Schematics(schematic_name)
            print(f'\nDEFINE_SCHEMATIC {schematic_name}')
            for element in schematic.Elements:
                self.output_element(element)
            print(f'END_SCHEMATIC {schematic_name}')
            print()
        while self.datafiles:
            datafile = self.datafiles.pop()
            print(f'INCLUDE "{datafile}"')


def object_to_dict(self):
    r = {}
    for a in dir(self):
        if a.startswith('_'):
            continue
        # splitting if allows us to skip value get sometimes
        try:
            value = getattr(self, a)
            if callable(value):
                continue
            elif isinstance(value, int) or isinstance(value, float):
                r[a] = value
            else:
                r[a] =  str(value)
        except Exception as e:
            print(f'Could not get value for attribute "{a}"')
            raise(e)       
    return r


if __name__ == "__main__":
    awrde = mwo.CMWOffice()
    open_example(awrde, 'LPF_Lumped.emp')
    element = awrde.Project.Schematics('LPF').Elements.Item(1)
    print(object_to_dict(element.DrawingObjects.Item(1)))
    