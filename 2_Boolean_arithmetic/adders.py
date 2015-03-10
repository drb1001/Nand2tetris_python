from ..1_Boolean_logic.multibit_gates import *

def HalfAdder(a,b):
    return ( XOR(a,b), AND(a,b) )

def FullAdder(a,b,c):
    return (0,0,0)

def Add16(a16,b16):
    return a16

def Inc16(a16):
    return a16
