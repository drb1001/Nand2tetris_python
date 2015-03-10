import unittest
from NAND import *

class TestGatesFunctions(unittest.TestCase):

    def test_NAND(self):
        self.assertEqual(NAND(0,0), 1)
        self.assertEqual(NAND(0,1), 1)
        self.assertEqual(NAND(1,0), 1)
        self.assertEqual(NAND(1,1), 0)


if __name__ == '__main__':
    unittest.main()
