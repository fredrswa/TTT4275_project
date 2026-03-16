import numpy as np
import matplotlib.pyplot as plt


from src.function import X

n0  = 2000
Fs  = 10 ** 6
dT  = 1/Fs
def X_sampled(n0, N):
    n = n0 + N - 1
    t = np.arange(n0*dT, n*dT, dT)
    X_t = X(t)
    #X_t = addGaussianNoise(X(t), dT)
    #X_t = addBiasNoise(X(t), dT)
    if n - n0 != np.size(t):
        print(__name__, ": t size does not correspond to n difference")
    return X_t
