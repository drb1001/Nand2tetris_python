from DFF import *
from Ch2_Boolean_arithmetic.ALU import *


def bit(in, load, time, delay = 0 ):
    return DFF( MUX( DFF( time - 1, ) in, load) , time, delay)


def register():
    return 0
