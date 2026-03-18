
import numpy as np

'''
Signal constants
'''
A       = 1 
f_0     = 10 ** 5
omega_0 = 2 * np.pi * f_0
phi     = np.pi/8

'''
Samling Size
'''
Fs  = 10 ** 6
T   = 1 / Fs
N   = 10000
P   = N*(N-1)/N 
Q   = N*(N-1)*(2*N-1)/6
n0  = -P/N

'''
Noise
'''   
SIGMA_R = 0.1
SIGMA_I = 0.1

