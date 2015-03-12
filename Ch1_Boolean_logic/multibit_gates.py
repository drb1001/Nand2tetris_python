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


def MUX16(a16, b16, sel):
    return [
            MUX(a16[0],b16[0],sel), MUX(a16[1],b16[1],sel), MUX(a16[2],b16[2],sel), MUX(a16[3],b16[3],sel),
            MUX(a16[4],b16[4],sel), MUX(a16[5],b16[5],sel), MUX(a16[6],b16[6],sel), MUX(a16[7],b16[7],sel),
            MUX(a16[8],b16[8],sel), MUX(a16[9],b16[9],sel), MUX(a16[10],b16[10],sel), MUX(a16[11],b16[11],sel),
            MUX(a16[12],b16[12],sel), MUX(a16[13],b16[13],sel), MUX(a16[14],b16[14],sel), MUX(a16[15],b16[15],sel)
            ]


def OR8WAY(a8):
    return OR( OR( OR( OR( OR( OR( OR(a8[0],a8[1]), a8[2]), a8[3]), a8[4]), a8[5]), a8[6]), a8[7])


def MUX4WAY16(a16, b16, c16, d16, sel2):

    return (
        OR16(

            OR16(

                OR16(

                    AND16(
                        AND16( a16, NOT16([ sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0] ]) )
                        ,
                        NOT16([ sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1] ])
                    )
                    ,

                    AND16(
                        AND16( b16, NOT16([ sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0] ]) )
                        ,
                        [ sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1] ]
                    )
                )
                ,

                AND16(
                    AND16( c16, [ sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0] ] )
                    ,
                    NOT16([ sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1] ])
                )
            ),

            AND16(
                AND16( d16, [ sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0],sel2[0] ] )
                ,
                [ sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1],sel2[1] ]
            )
        )
    )


def MUX8WAY16(a16, b16, c16, d16, e16, f16, g16, h16, sel3):

    return MUX16(
        MUX4WAY16( a16, b16, c16, d16, sel3[1:] ),
        MUX4WAY16( e16, f16, g16, h16, sel3[1:] ),
        sel3[0]
        )



def DMUX4WAY(a, sel2):
    return (
            AND( NOT(sel2[0]), DMUX(a,sel2[1])[0] ),
            AND( NOT(sel2[0]), DMUX(a,sel2[1])[1] ),
            AND( sel2[0], DMUX(a,sel2[1])[0] ),
            AND( sel2[0], DMUX(a,sel2[1])[1] )
            )

def DMUX8WAY(a, sel3):
    return (
            AND( NOT(sel3[0]), DMUX4WAY(a,sel3[1:])[0] ),
            AND( NOT(sel3[0]), DMUX4WAY(a,sel3[1:])[1] ),
            AND( NOT(sel3[0]), DMUX4WAY(a,sel3[1:])[2] ),
            AND( NOT(sel3[0]), DMUX4WAY(a,sel3[1:])[3] ),
            AND( (sel3[0]), DMUX4WAY(a,sel3[1:])[0] ),
            AND( (sel3[0]), DMUX4WAY(a,sel3[1:])[1] ),
            AND( (sel3[0]), DMUX4WAY(a,sel3[1:])[2] ),
            AND( (sel3[0]), DMUX4WAY(a,sel3[1:])[3] )
            )
