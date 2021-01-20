""" This file tests the API wrappers for the AWRDE COM API

    Due to the volume of calls in the API it is not practical to exhaustively test the API
    so these are just spot checks of the API functionality.
"""
import os
import pytest
import mwoffice as mwo
import pdb

@pytest.fixture
def awrde() -> mwo.CMWOffice:
    global awrde  # type: mwo.CMWOffice
    awrde = mwo.CMWOffice()
    awrde.TestMode = 1
    test_project = os.path.join(os.path.dirname(__file__), '..', 'testdata', 'lpf_lumped.emp')
    try:
        awrde.Project.Name
    except:
        print('Opening lpf_lumped.emp')
        awrde.Open(test_project)

    if awrde.Project.Name != 'lpf_lumped.emp':
        awrde.Project.Close(False)
        awrde.Open(test_project)
    return awrde


def test_project_graphs(awrde: mwo.CMWOffice):
    # get as a list
    graphs = awrde.Project.Graphs
    l = list(graphs)
    assert len(l) > 0

    first_graph = l[0]
    assert isinstance(first_graph.Name, str)  # get the name of the graph
    graph = awrde.Project.Graphs('Group Delay')  # get graph by name
    assert graph.Name == 'Group Delay'
    assert len(list(graph.Measurements)) == 1
    orig_num_graphs = len(l)
    graphs.Add('Test Graph 1', mwo.mwGraphType.mwGT_Tabular)
    assert graphs.Count == orig_num_graphs + 1  # test count also
    graphs.Remove('Test Graph 1')
    assert graphs.Count == orig_num_graphs

    # test item accessor
    g1 =  graphs.Item(1)
    assert g1.Name == first_graph.Name

    # test exists
    assert graphs.Exists('Group Delay') == True
    assert graphs.Exists('Dummy') == False




def test_project_schematics(awrde: mwo.CMWOffice):
    schematics = awrde.Project.Schematics
    l = list(schematics)
    assert len(l) > 0
    first_schematic = l[0]
    assert isinstance(first_schematic.Name, str)  # get the name of the schematic
    sch = awrde.Project.Schematics('LPF')  # get schematic by name
    assert sch.Name == 'LPF'
    assert len(list(sch.Elements)) > 0  # make sure there are elements
    orig_num_sch = len(l)
    schematics.Add('Test Schematic 1')
    assert schematics.Count == orig_num_sch + 1  # test count also
    schematics.Remove('Test Schematic 1')
    assert schematics.Count == orig_num_sch

    # test item accessor
    assert schematics.Item(1).Name == first_schematic.Name

    # test exists
    assert schematics.Exists('LPF') == True
    assert schematics.Exists('Dummy') == False
    

def test_project_datafiles(awrde: mwo.CMWOffice):
    datafiles = awrde.Project.DataFiles
    l = list(datafiles)
    assert len(l) > 0
    df = l[0]
    assert df.Type == 0
    assert mwo.mwDataFileType(df.Type)._name_ == 'mwDFT_SNP'


def test_models(awrde: mwo.CMWOffice):
    model = awrde.Models.Item(1000)
    assert isinstance(model.Name, str)
    assert model.NodeCount > 0
    parameters = list(model.ParameterDefinitions)
    p = parameters[0]
    assert isinstance(p.Name, str)
    assert isinstance(p.Description, str)

    model = awrde.Models('MLIN')
    assert model.NodeCount == 2
    p = model.ParameterDefinitions(3)
    assert p.Name == 'L'
    assert p.Description == 'Conductor Length'
    assert mwo.mwUnitType(p.UnitType)._name_ == 'mwUT_Length'


def test_measurement_sweeplabels(awrde: mwo.CMWOffice):
    awrde.Project.Simulate()  # required to access measurement data
    meas = awrde.Project.Graphs('Group Delay').Measurements(1)
    # Sweep Labels are not consistent
    # graph.Measurements returns a Measurements object
    # but meas.SweepLabels returns a function rather than a SweepLabels object
    assert callable(meas.SweepLabels)
    sl = meas.SweepLabels(1)


def test_designnotes(awrde: mwo.CMWOffice):
    dn = awrde.Project.DesignNotes(1)
    assert "lumped element filter" in dn.PlainText

    # test generator
    dn = list(awrde.Project.DesignNotes)[0]
    assert "lumped element filter" in dn.PlainText


def test_directories(awrde: mwo.CMWOffice):
    dirs = {x.Name: x.Value for x in list(awrde.Directories)}
    assert 'AppDir' in dirs
    assert 'Examples' in dirs
    assert os.path.exists(dirs['AppDataCommon'])


def test_options(awrde: mwo.CMWOffice):
    opts = {x.Name: x.Value for x in list(awrde.Options)}
    assert isinstance(opts['SchemEquationFontSize'], int)
    assert isinstance(opts['LayoutPrintScaleFactor'], float)


def test_slices(awrde: mwo.CMWOffice):
    awrde = mwo.CMWOffice()

    frequency_objects = awrde.Project.Frequencies
    assert frequency_objects[0].Value == 0.1e9
    assert frequency_objects[-1].Value == 1.0e9
    frequency_list = [f.Value for f in frequency_objects[:5]]
    assert len(frequency_list) == 5


def test_str(awrde: mwo.CMWOffice):
    assert str(awrde.Project) == 'CProject(lpf_lumped.emp)'  # object is in form class(value of Name property)
    assert str(awrde.Project.Schematics) == 'CSchematics(1)'  # collection is of the form class(number of objects)
    assert str(awrde.Project.Schematics[0]) == 'CSchematic(LPF)'