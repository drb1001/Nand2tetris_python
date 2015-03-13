def DFF(a,t):
    return (a,t+1)


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
