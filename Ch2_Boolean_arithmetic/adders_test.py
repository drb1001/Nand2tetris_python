import unittest
from adders import *


class TestAddersFunctions(unittest.TestCase):

    def test_HalfAdder(self):
        self.assertEqual( HalfAdder(0,0), (0,0) )
        self.assertEqual( HalfAdder(0,1), (1,0) )
        self.assertEqual( HalfAdder(1,0), (1,0) )
        self.assertEqual( HalfAdder(1,1), (0,1) )

    def test_FullAdder(self):
        self.assertEqual( FullAdder(0,0,0), (0,0) )
        self.assertEqual( FullAdder(0,0,1), (1,0) )
        self.assertEqual( FullAdder(0,1,0), (1,0) )
        self.assertEqual( FullAdder(0,1,1), (0,1) )
        self.assertEqual( FullAdder(1,0,0), (1,0) )
        self.assertEqual( FullAdder(1,0,1), (0,1) )
        self.assertEqual( FullAdder(1,1,0), (0,1) )
        self.assertEqual( FullAdder(1,1,1), (1,1) )

    def test_Add16(self):
        self.assertEqual( Add16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] ), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( Add16( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] )
        self.assertEqual( Add16( [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0] )
        self.assertEqual( Add16( [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] ), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] )
        self.assertEqual( Add16( [0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1], [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0] ), [0,1,0,0,1,1,0,0,1,0,1,1,0,0,1,1] )
        self.assertEqual( Add16( [0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0], [1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0] ), [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0] )


    def test_Inc16(self):
        self.assertEqual( Inc16([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] )
        self.assertEqual( Inc16([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )
        self.assertEqual( Inc16([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1]), [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0] )
        self.assertEqual( Inc16([1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0] )



if __name__ == '__main__':
    unittest.main()
