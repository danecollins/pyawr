import unittest

from pyawr.helpers import *
from pyawr.enum_map import mwCellStretcherAttributes, mwDataSetFlags

awr, awrc = connect()


class TestConstants(unittest.TestCase):
    def test_constant_definitions(self):
        self.assertEqual(awrc.mwAAT_BuildRevision, 14)
        self.assertEqual(awrc.mwAFT_FlexLmLicense, 5)
        self.assertEqual(awrc.mwCSA_ParameterName, 1)

    def test_reverse_mapping(self):
        self.assertEqual(mwCellStretcherAttributes(awrc.mwCSA_IsBound), 'mwCSA_IsBound')
        self.assertEqual(mwDataSetFlags(awrc.mwDSF_PortOnly), 'mwDSF_PortOnly')


class TestUtilityFunctions(unittest.TestCase):
    def test_vbrange(self):
        self.assertEqual(vbrange(5), range(1, 6))

    def test_open_example(self):
        open_example(awr, 'LPF_lumped.emp')
        expected = ['Passband and Stopband', 'Input Match', 'Group Delay', 'Output Match']
        graphs = [x.Name for x in awr.Project.Graphs]
        self.assertCountEqual(graphs, expected)

    def test_meas_from_graph(self):
        open_example(awr, 'LPF_lumped.emp')
        measurements = meas_from_graph('Passband and Stopband')
        self.assertEqual(len(measurements), 3)
        expected = ['LPF:DB(|S(1,1)|)', 'LPF:DB(|S(2,1)|)', 'LPF:DB(|S(2,2)|)']
        for m in measurements:
            self.assertTrue(m.Name in expected)

class TestAwrMeas(unittest.TestCase):
    def test_create(self):
        open_example(awr, 'LPF_lumped.emp')
        awr.Project.Simulate()
        m = awr.Project.Graphs('Passband and Stopband').Measurements('LPF:DB(|S(2,1)|)')
        am = AwrMeas(m)
        self.assertEqual(am.source, 'LPF')
        self.assertEqual(am.name, 'DB(|S(2,1)|)')
        self.assertEqual(am.plot_dim, 2)
        self.assertEqual(am.data_type, 'mwMDT_ReflectionData')
        self.assertEqual(am.x_units, 'mwUT_Frequency')
        self.assertEqual(am.y_units, 'mwUT_None')
        self.assertEqual(len(am.df), 95)


if __name__ == '__main__':
    unittest.main()