'''
Module Name: fanning_factor.py
Purpose: Calculate Fanning Friction Factor (dimensionless) using 3 known equation: Jain, Swanne-Jain,and Chen
Author: Mico Siahaan
License: GPL

The inputs of each equation will be:
    roughness : relative roughness of the pipe 
    D : average inside diameter of the pipe (feet)
    Re : Reynold number (dimensionless)
'''

from math import log

def jain(roughness, D, Re):
    fanning = 1/(2.28 - 4*log(roughness/D + (29.843/Re)**0.9))**2
    return fanning

def swanne_jain(roughness, D, Re):
    fanning = 1/(4*log((6.97/Re)**0.9 + (roughness/D)/3.7))**2
    return fanning

def chen(roughness, D, Re):
    A = (roughness/D)**1.1098/2.8257 + (7.149/Re)**0.8981
    fanning = 1/(4*log((roughness/D)/3.7 - 5.0452/Re * log(A)))**2
    return fanning

# Test Comparing results
 
if __name__ == '__main__':
    
    roughness = 0.00015
    D = 15/12
    Re = 83064

    print 'Fanning (Jain Equation) = %s ' % (jain(roughness,D,Re))
    print 'Fanning (Swanne-Jain Equation) = %s ' % (swanne_jain(roughness,D,Re))
    print 'Fanning (Chen Equation) = %s ' % (chen(roughness,D,Re))
