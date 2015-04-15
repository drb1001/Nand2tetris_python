import time


def clock(start, end, delay = 1):
    
    sleep(delay)


def DFF(a, time, delay = 0):

    if time < 0: time = 0
    return (a, time + 1)


# NOTES:
#
# DFF(a,t) = DFF(a,t+1)
#
# out(t) = in(t-1)
# in(t) = out(t+1)


#           a     t
#           |     |
#          \|/   \|/
#       _ _ _ _ _ _ _ _
#      |                |
#      |      DFF       | <----  clock
#      |_ _ _ _ _ _ _ _ |
#           |     |
#           |     |
#          \|/   \|/
#           b     t
#
#
