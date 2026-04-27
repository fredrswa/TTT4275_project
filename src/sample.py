import numpy as np
import matplotlib.pyplot as plt

from constants import A, f_0, omega_0, phi, n0, N, T


def X(t):
    return A * np.exp((omega_0 * t + phi)*1j)

def addGaussianNoise(x_t, sigma):
    N = np.size(x_t)
    Z_t = x_t + np.random.normal(0,sigma, N) + 1j * np.random.normal(0, sigma, N)
    return Z_t

def addBias(x_t):
    # Currently not implemented, and not required, but might be cool to test
    # Will probably have to extend state vector
    Z_t = x_t
    return Z_t

def Z(sigma):
    n = n0 + N - 1
    t = np.arange(n0*T, n*T, T)
    
    Z_t = addGaussianNoise(X(t), sigma)
    #Z_t = addBiasNoise(X(t), T)
    return Z_t
