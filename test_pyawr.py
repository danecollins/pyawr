import unittest

from pyawr import *
from cmap import mwCellStretcherAttributes, mwDataSetFlags

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
    def test_vbr(self):
        self.assertEqual(vbr(5), range(1, 6))

    def test_as_list(self):
        pass



if __name__ == '__main__':
    unittest.main()