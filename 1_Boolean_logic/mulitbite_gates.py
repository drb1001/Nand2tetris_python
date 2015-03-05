from gates import *

# Multibit gates

def NOT16(array16):
    return [ NOT(array16[0]), NOT(array16[1]), NOT(array16[2]), NOT(array16[3]),
            NOT(array16[4]), NOT(array16[5]), NOT(array16[6]), NOT(array16[7]),
            NOT(array16[8]), NOT(array16[9]), NOT(array16[10]), NOT(array16[11]),
            NOT(array16[12]), NOT(array16[13]), NOT(array16[14]), NOT(array16[15]) ]

def AND16(a16, b16):
    return [ NOT(array16[0]), NOT(array16[1]), NOT(array16[2]), NOT(array16[3]),
            NOT(array16[4]), NOT(array16[5]), NOT(array16[6]), NOT(array16[7]),
            NOT(array16[8]), NOT(array16[9]), NOT(array16[10]), NOT(array16[11]),
            NOT(array16[12]), NOT(array16[13]), NOT(array16[14]), NOT(array16[15]) ]
