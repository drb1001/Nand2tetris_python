import unittest
from gates import *


class TestGatesFunctions(unittest.TestCase):

    def test_NOT(self):
        self.assertEqual(NOT(1), 0)
        self.assertEqual(NOT(0), 1)

    def test_AND(self):
        self.assertEqual(AND(0,0), 0)
        self.assertEqual(AND(0,1), 0)
        self.assertEqual(AND(1,0), 0)
        self.assertEqual(AND(1,1), 1)

    def test_OR(self):
        self.assertEqual(OR(0,0), 0)
        self.assertEqual(OR(0,1), 1)
        self.assertEqual(OR(1,0), 1)
        self.assertEqual(OR(1,1), 1)

    def test_NOR(self):
        self.assertEqual(NOR(0,0), 1)
        self.assertEqual(NOR(0,1), 0)
        self.assertEqual(NOR(1,0), 0)
        self.assertEqual(NOR(1,1), 0)

    def test_XOR(self):
        self.assertEqual(XOR(0,0), 0)
        self.assertEqual(XOR(0,1), 1)
        self.assertEqual(XOR(1,0), 1)
        self.assertEqual(XOR(1,1), 0)

    def test_XNOR(self):
        self.assertEqual(XNOR(0,0), 1)
        self.assertEqual(XNOR(0,1), 0)
        self.assertEqual(XNOR(1,0), 0)
        self.assertEqual(XNOR(1,1), 1)

    def test_MUX(self):
        self.assertEqual(MUX(0,0,0), 0)
        self.assertEqual(MUX(0,1,0), 0)
        self.assertEqual(MUX(1,0,0), 1)
        self.assertEqual(MUX(1,1,0), 1)
        self.assertEqual(MUX(0,0,1), 0)
        self.assertEqual(MUX(0,1,1), 1)
        self.assertEqual(MUX(1,0,1), 0)
        self.assertEqual(MUX(1,1,1), 1)

    def test_DMUX(self):
        self.assertEqual(DMUX(0,0), (0,0))
        self.assertEqual(DMUX(1,0), (1,0))
        self.assertEqual(DMUX(0,1), (0,0))
        self.assertEqual(DMUX(1,1), (0,1))


    def test_NOT16(self):
        self.assertEqual( NOT16([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] )
        self.assertEqual( NOT16([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( NOT16([0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0]), [1,0,0,1,1,0,0,1,1,1,1,1,1,1,0,1] )
        self.assertEqual( NOT16([1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0]), [0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1] )
        self.assertEqual( NOT16([0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,1]), [1,1,1,0,0,1,1,1,1,0,1,1,1,0,0,0] )


    def test_AND16(self):
        self.assertEqual( AND16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( AND16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( AND16( [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] )
        self.assertEqual( AND16( [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( AND16( [0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1], [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0]), [0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0] )
        self.assertEqual( AND16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0]), [0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0] )


    # def test_OR16(self):
    #
    #
    # def test_MUX16(self):
    #
    #
    # def test_MUX4WAY16(self):
    #
    #
    # def test_MUX8WAY16(self):
    #
    #
    # def test_DMUX4WAY(self):
    #
    #
    # def test_DMUX8WAY(self):
    #





if __name__ == '__main__':
    unittest.main()
