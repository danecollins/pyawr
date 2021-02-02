""" This file tests the API wrappers for the AWRDE COM API

    Due to the volume of calls in the API it is not practical to exhaustively test the API
    so these are just spot checks of the API functionality.
"""
import os
import pytest
import pyawr.mwoffice as mwo
from helpers import AwrMeasurement, Netlister

@pytest.fixture
def awrde() -> mwo.CMWOffice:
    global awrde  # type: mwo.CMWOffice
    awrde = mwo.CMWOffice()
    awrde._CMWOffice__IMWOffice.testmode=True
    test_project = os.path.join(os.path.dirname(__file__), '..', 'testdata', 'lpf_lumped.emp')
    try:
        awrde.Project.Name
    except:
        print('Opening lpf_lumped.emp')
        awrde.Open(test_project)

    if awrde.Project.Name != 'lpf_lumped.emp':
        awrde.Project.Close(False, '')
        awrde.Open(test_project)
    return awrde


def test_awr_measurement(awrde: mwo.CMWOffice):
    # get as a list
    awrde.Project.Simulate()
    m = awrde.Project.Graphs[0].Measurements[0]
    parsed_measurement = AwrMeasurement(m)
    assert parsed_measurement.name == 'DB(|S(1,1)|)'
    assert parsed_measurement.source == 'LPF'
    assert parsed_measurement.data_type == 'mwMDT_ReflectionData'
    assert parsed_measurement.plot_dim == 2
    assert parsed_measurement.x_units == 'mwUT_Frequency'
    assert parsed_measurement.y_units == 'mwUT_None'

    
def test_parse_meas_string():
    s = 'Pulse Signal.HS:Vtime(PORT_1,1)[*]'
    (source, meas_name, simulator) = AwrMeasurement.parse_meas_string(s)
    assert source  == 'Pulse Signal'
    assert simulator == 'HS'
    assert meas_name  == 'Vtime(PORT_1,1)[*]'


def test_netlister(awrde, capsys):
    s = awrde.Project.Schematics('LPF')
    netlister = Netlister(awrde, s)
    netlister.generate()
    out, err = capsys.readouterr()
    assert "GND pin(1)=node(0)" in out
    assert "CAP pin(1)=node(0) pin(2)=node(4) ID=C1 C=9.596" in out

