
import numpy as np
import cmath


A       = 1 
f_0     = 10 ** 5
omega_0 = 2 * np.pi * f_0
phi     = np.pi/8

def X(t):
    return A * np.exp((omega_0 * t + phi)*1j)
