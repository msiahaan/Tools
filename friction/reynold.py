'''
Module Name: reynold.py
Purpose: Calculating reynold dimensionless factor
License: GPL

Inputs of the method will be:
    Q : flowrate of the fluid (BPH)
    d : inside dimater of the pipe (in)
    kv : kinematic viscosity of the fluid (cSt)
'''

def reynold(Q,d,kv):
    return 2214*Q/(d*kv)

# test
if __name__ == '__main__':
    Q = 4500/24
    d = 6.065
    kv = 3.02

    print 'Reynold number: %s' % (reynold(Q,d,kv))    