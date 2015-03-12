from Ch1_Boolean_logic.multibit_gates import *

def HalfAdder(a,b):
    return ( XOR(a,b), AND(a,b) )

def FullAdder(a,b,c):
    return (
        HalfAdder( HalfAdder(a,b)[0], c )[0] ,
        OR( HalfAdder(a,b)[1] , HalfAdder( HalfAdder(a,b)[0], c )[1] )
        )

def Add16(a16,b16):
    return a16

def Inc16(a16):
    return Add16(a16,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
