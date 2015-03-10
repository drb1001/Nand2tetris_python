from NAND import *


# simple gates

def NOT(a):
    return NAND(1,a)

def AND(a,b):
    return NOT(NAND(a,b))

def NOR(a,b):
    return AND(NOT(a),NOT(b))

def OR(a,b):
    return NOT(NOR(a,b))

def XOR(a,b):
    return AND(NOT(AND(a,b)),OR(a,b))

def XNOR(a,b):
    return NOT(XOR(a,b))


# MUX / DMUX

def MUX(a,b,sel):
    return OR(AND(NOT(sel),a),AND(sel,b))

def DMUX(a,sel):
    return  ( AND(a,NOT(sel)) , AND(a,sel) )
