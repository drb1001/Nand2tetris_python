from Ch1_Boolean_logic.multibit_gates import *

def HalfAdder(a,b):
    return ( XOR(a,b), AND(a,b) )

def FullAdder(a,b,c):
    return (
        HalfAdder( HalfAdder(a,b)[0], c )[0] ,
        OR( HalfAdder(a,b)[1] , HalfAdder( HalfAdder(a,b)[0], c )[1] )
        )

def Add16(a16,b16):
    sum15  = HalfAdder( a16[15], b16[15] )
    sum14  = FullAdder( a16[14], b16[14], sum15[1] )
    sum13  = FullAdder( a16[13], b16[13], sum14[1] )
    sum12  = FullAdder( a16[12], b16[12], sum13[1] )
    sum11  = FullAdder( a16[11], b16[11], sum12[1] )
    sum10  = FullAdder( a16[10], b16[10], sum11[1] )
    sum9  = FullAdder( a16[9], b16[9], sum10[1] )
    sum8  = FullAdder( a16[8], b16[8], sum9[1] )
    sum7  = FullAdder( a16[7], b16[7], sum8[1] )
    sum6  = FullAdder( a16[6], b16[6], sum7[1] )
    sum5 = FullAdder( a16[5], b16[5], sum6[1] )
    sum4 = FullAdder( a16[4], b16[4], sum5[1] )
    sum3 = FullAdder( a16[3], b16[3], sum4[1] )
    sum2 = FullAdder( a16[2], b16[2], sum3[1] )
    sum1 = FullAdder( a16[1], b16[1], sum2[1] )
    sum0 = FullAdder( a16[0], b16[0], sum1[1] )

    return [
            sum0[0],
            sum1[0],
            sum2[0],
            sum3[0],
            sum4[0],
            sum5[0],
            sum6[0],
            sum7[0],
            sum8[0],
            sum9[0],
            sum10[0],
            sum11[0],
            sum12[0],
            sum13[0],
            sum14[0],
            sum15[0]
            ]

def Inc16(a16):
    return Add16(a16,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
