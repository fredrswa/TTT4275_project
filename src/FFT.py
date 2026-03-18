
import numpy as np

import scipy as sp
from constants import SIGMA_I, SIGMA_R, P, Q, N, T, n0


# def FFT(z):
    
#     yfreq = sp.fft.fft(z)
#     xfreq = sp.fft.fftfreq(N, d=T/N)

#     return (1/N) * np.sum(z * np.exp(-1j * 2 * np.pi * xfreq * n0 * T))


