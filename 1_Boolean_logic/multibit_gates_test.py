import unittest
from multibit_gates import *


class TestGatesFunctions(unittest.TestCase):


    def test_NOT16(self):
        self.assertEqual( NOT16([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] )
        self.assertEqual( NOT16([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( NOT16([0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0]), [1,0,0,1,1,0,0,1,1,1,1,1,1,1,0,1] )
        self.assertEqual( NOT16([1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0]), [0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1] )
        self.assertEqual( NOT16([0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,1]), [1,1,1,0,0,1,1,1,1,0,1,1,1,0,0,0] )

    def test_AND16(self):
        self.assertEqual( AND16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( AND16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( AND16( [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] )
        self.assertEqual( AND16( [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( AND16( [0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1], [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0] ), [0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0] )
        self.assertEqual( AND16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0] ), [0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0] )

    def test_OR16(self):
        self.assertEqual( OR16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( OR16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] )
        self.assertEqual( OR16( [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] )
        self.assertEqual( OR16( [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] ), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] )
        self.assertEqual( OR16( [0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1], [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0] ), [0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1] )
        self.assertEqual( OR16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0] ), [1,0,0,1,1,0,1,0,0,1,1,1,0,1,1,0] )

    def test_MUX16(self):
        self.assertEqual( MUX16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0 ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 1 ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], 0 ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], 1 ), [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0] )
        self.assertEqual( MUX16( [1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0 ), [1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0] )
        self.assertEqual( MUX16( [1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 1 ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX16( [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1], 0 ), [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0] )
        self.assertEqual( MUX16( [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1], 1 ), [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] )

    def test_OR8WAY(self):
        self.assertEqual( OR8WAY([0,0,0,0,0,0,0,0]), 0)
        self.assertEqual( OR8WAY([1,1,1,1,1,1,1,1]), 1)
        self.assertEqual( OR8WAY([0,0,0,1,0,0,0,0]), 1)
        self.assertEqual( OR8WAY([0,0,0,0,0,0,0,1]), 1)
        self.assertEqual( OR8WAY([0,0,1,0,0,1,1,0]), 1)

    def test_MUX4WAY16(self):
        self.assertEqual( MUX4WAY16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX4WAY16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,1] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX4WAY16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,0] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX4WAY16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX4WAY16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0], [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1], [0,0] ), [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0] )
        self.assertEqual( MUX4WAY16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0], [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1], [0,1] ), [1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0] )
        self.assertEqual( MUX4WAY16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0], [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1], [1,0] ), [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0] )
        self.assertEqual( MUX4WAY16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0], [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1], [1,1] ), [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] )

    def test_MUX8WAY16(self):
        self.assertEqual( MUX8WAY16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX8WAY16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,1] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX8WAY16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,1,0] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX8WAY16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,1,1] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX8WAY16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,0,0] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX8WAY16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,0,1] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX8WAY16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,0] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX8WAY16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,1] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( MUX8WAY16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1], [0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0], [0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1], [0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0], [0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1], [0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0], [1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1], [0,0,0] ), [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0] )
        self.assertEqual( MUX8WAY16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1], [0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0], [0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1], [0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0], [0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1], [0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0], [1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1], [0,0,1] ), [0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1] )
        self.assertEqual( MUX8WAY16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1], [0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0], [0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1], [0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0], [0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1], [0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0], [1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1], [0,1,0] ), [0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0] )
        self.assertEqual( MUX8WAY16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1], [0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0], [0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1], [0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0], [0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1], [0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0], [1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1], [0,1,1] ), [0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1] )
        self.assertEqual( MUX8WAY16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1], [0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0], [0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1], [0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0], [0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1], [0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0], [1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1], [1,0,0] ), [0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0] )
        self.assertEqual( MUX8WAY16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1], [0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0], [0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1], [0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0], [0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1], [0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0], [1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1], [1,0,1] ), [0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1] )
        self.assertEqual( MUX8WAY16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1], [0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0], [0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1], [0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0], [0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1], [0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0], [1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1], [1,1,0] ), [0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0] )
        self.assertEqual( MUX8WAY16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1], [0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0], [0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1], [0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0], [0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1], [0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0], [1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1], [1,1,1] ), [1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1] )

    def test_DMUX4WAY(self):
        self.assertEqual( (DMUX4WAY(0, [0,0]) ), (0,0,0,0) )
        self.assertEqual( (DMUX4WAY(0, [0,1]) ), (0,0,0,0) )
        self.assertEqual( (DMUX4WAY(0, [1,0]) ), (0,0,0,0) )
        self.assertEqual( (DMUX4WAY(0, [1,1]) ), (0,0,0,0) )
        self.assertEqual( (DMUX4WAY(1, [0,0]) ), (1,0,0,0) )
        self.assertEqual( (DMUX4WAY(1, [0,1]) ), (0,1,0,0) )
        self.assertEqual( (DMUX4WAY(1, [1,0]) ), (0,0,1,0) )
        self.assertEqual( (DMUX4WAY(1, [1,1]) ), (0,0,0,1) )

    def test_DMUX8WAY(self):
        self.assertEqual( DMUX8WAY(0, [0,0,0]), (0,0,0,0,0,0,0,0) )
        self.assertEqual( DMUX8WAY(0, [0,0,1]), (0,0,0,0,0,0,0,0) )
        self.assertEqual( DMUX8WAY(0, [0,1,0]), (0,0,0,0,0,0,0,0) )
        self.assertEqual( DMUX8WAY(0, [0,1,1]), (0,0,0,0,0,0,0,0) )
        self.assertEqual( DMUX8WAY(0, [1,0,0]), (0,0,0,0,0,0,0,0) )
        self.assertEqual( DMUX8WAY(0, [1,0,1]), (0,0,0,0,0,0,0,0) )
        self.assertEqual( DMUX8WAY(0, [1,1,0]), (0,0,0,0,0,0,0,0) )
        self.assertEqual( DMUX8WAY(0, [1,1,1]), (0,0,0,0,0,0,0,0) )
        self.assertEqual( DMUX8WAY(1, [0,0,0]), (1,0,0,0,0,0,0,0) )
        self.assertEqual( DMUX8WAY(1, [0,0,1]), (0,1,0,0,0,0,0,0) )
        self.assertEqual( DMUX8WAY(1, [0,1,0]), (0,0,1,0,0,0,0,0) )
        self.assertEqual( DMUX8WAY(1, [0,1,1]), (0,0,0,1,0,0,0,0) )
        self.assertEqual( DMUX8WAY(1, [1,0,0]), (0,0,0,0,1,0,0,0) )
        self.assertEqual( DMUX8WAY(1, [1,0,1]), (0,0,0,0,0,1,0,0) )
        self.assertEqual( DMUX8WAY(1, [1,1,0]), (0,0,0,0,0,0,1,0) )
        self.assertEqual( DMUX8WAY(1, [1,1,1]), (0,0,0,0,0,0,0,1) )



if __name__ == '__main__':
    unittest.main()
