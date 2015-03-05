from gates import *

# Multibit gates

def NOT16(a16):
    return [
            NOT(a16[0]), NOT(a16[1]), NOT(a16[2]), NOT(a16[3]),
            NOT(a16[4]), NOT(a16[5]), NOT(a16[6]), NOT(a16[7]),
            NOT(a16[8]), NOT(a16[9]), NOT(a16[10]), NOT(a16[11]),
            NOT(a16[12]), NOT(a16[13]), NOT(a16[14]), NOT(a16[15])
            ]

def AND16(a16, b16):
    return [
            AND(a16[0],b16[0]), AND(a16[1],b16[1]), AND(a16[2],b16[2]), AND(a16[3],b16[3]),
            AND(a16[4],b16[4]), AND(a16[5],b16[5]), AND(a16[6],b16[6]), AND(a16[7],b16[7]),
            AND(a16[8],b16[8]), AND(a16[9],b16[9]), AND(a16[10],b16[10]), AND(a16[11],b16[11]),
            AND(a16[12],b16[12]), AND(a16[13],b16[13]), AND(a16[14],b16[14]), AND(a16[15],b16[15])
            ]

def OR16(a16, b16):
    return [
            OR(a16[0],b16[0]), OR(a16[1],b16[1]), OR(a16[2],b16[2]), OR(a16[3],b16[3]),
            OR(a16[4],b16[4]), OR(a16[5],b16[5]), OR(a16[6],b16[6]), OR(a16[7],b16[7]),
            OR(a16[8],b16[8]), OR(a16[9],b16[9]), OR(a16[10],b16[10]), OR(a16[11],b16[11]),
            OR(a16[12],b16[12]), OR(a16[13],b16[13]), OR(a16[14],b16[14]), OR(a16[15],b16[15])
            ]
