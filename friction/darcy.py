'''
Module Name : darcy.py
Purpose: Calculate pressure drop in pipeline system using Darcy-Weisbach Equation
Author: Mico Siahaan
License: GPL


Inputs will be:
    L : length of the pipeline (ft)
    d : average inside diameter of the pipe (in)
    Q : flowrate of the fluid (BPH)
    kv : kinematic viscosity of the fluid
    roughness: relative roughness of the pipe
    
Constant:
    g : gravitional constant (32.174 ft/sec2)
Output:
    hf: pressure drop (ft of liquid)
Darcy-Weisbach Equation:
    hf = f * L * v**2 / (D*2*32.174)
'''

from reynold import reynold
from fanning_factor import chen

def frict_losses(Q, d, L, kv, roughness):
    NRe = reynold(Q, d, kv)
    D = d/12
    # Using Chen Equation to calculate friction factor
    f = 4 * chen(roughness, D, NRe)
    # Calculate velocity
    v = 0.2860* Q / d**2
    hf = f * L * v**2 / (D*2* 32.174)
    return (NRe,f,v,hf)

if __name__ == '__main__':
    Q = 60382.2/24
    d = 15
    L = 128* 3280.84
    sg = 0.87
    kv = 3.8
    roughness = 0.00015

    (NRe,f,v,hf) = frict_losses(Q,d,L,kv,roughness)
    
    print 'Reynold number: %s' % NRe
    print 'Fanning friction factor: %s' % f
    print 'Fluid velocity: %s ft/s' % v
    print 'Pressure drop of system: %s  psi' % (hf*sg*0.433)      

    

