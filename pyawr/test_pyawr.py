
from pyawr.helpers import *

awr = connect()


def test_vbrange():
    assert vbrange(5) == range(1, 6)

def test_open_example():
    open_example(awr, 'LPF_lumped.emp')
    expected = ['Passband and Stopband', 'Input Match', 'Group Delay', 'Output Match', 'Windowed Max to Min Response']
    graphs = [x.Name for x in awr.Project.Graphs]
    assert graphs == expected


def test_meas_from_graph():
    open_example(awr, 'LPF_lumped.emp')
    measurements = meas_from_graph(awr, 'Passband and Stopband')
    assert len(measurements) == 3
    expected = ['LPF:DB(|S(1,1)|)', 'LPF:DB(|S(2,1)|)', 'LPF:DB(|S(2,2)|)']
    actual = [m.Name for m in measurements]
    assert actual == expected


def test_create():
    open_example(awr, 'LPF_lumped.emp')
    awr.Project.Simulate()
    m = awr.Project.Graphs('Passband and Stopband').Measurements('LPF:DB(|S(2,1)|)')
    am = AwrMeas(m)
    assert am.source == 'LPF'
    assert am.name == 'DB(|S(2,1)|)'
    assert am.plot_dim == 2
    assert am.data_type == 'mwMDT_ReflectionData'
    assert am.x_units == 'mwUT_Frequency'
    assert am.y_units == 'mwUT_None'
    assert len(am.df) == 95


def test_meas_to_df():
    open_example(awr, 'LPF_lumped.emp')
    awr.Project.Simulate()
    m = awr.Project.Graphs('Passband and Stopband').Measurements('LPF:DB(|S(2,1)|)')
    am = AwrMeas(m)
    df = am.meas_to_df()
    assert min(df.x) == 1e8
    assert max(df.x) == 1e9
    