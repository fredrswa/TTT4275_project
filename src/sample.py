import numpy as np
import matplotlib.pyplot as plt

from src.function import X
import constants




n0      = constants.n0
N       = constants.N
T       = constants.T


def addGaussianNoise(x_t, T, sigma):
    sigma_i = sigma
    sigma_r = sigma
    N = np.size(x_t)
    noice = np.random.normal(0, sigma_r, (1, N)) + 1j * np.random.normal(0, sigma_i, (1, N))
    Z_t = x_t + noice
    return Z_t  

def addBias(x_t, T):
    # Currently not implemented, and not required, but might be cool to test
    # Will probably have to extend state vector
    Z_t = x_t
    return Z_t

def Z(sigma):
    n = np.arange(n0, N+n0)
    t = n*T
    
    Z_t = addGaussianNoise(X(t), T, sigma)
    #Z_t = addBiasNoise(X(t), T)
    return Z_t
