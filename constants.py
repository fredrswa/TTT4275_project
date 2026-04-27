import numpy as np

'''
Samling Size
'''
Fs  = 10 ** 6
T   = 1 / Fs
N   = 513
P   = N*(N-1)/2 
Q   = N*(N-1)*(2*N-1)/6
#n0  = -P/N
n0  = -256

'''
Noise
'''   
SNR_DECIBEL = np.array([-10 + i * 10 for i in range(8)])
SNR_LINEAR  = 10**(SNR_DECIBEL/10)
SIGMA_SNR = np.sqrt(1 / (2 * SNR_LINEAR))

'''
FFT
'''
FFT_SIZES = 2 ** np.array([10, 12, 14, 16, 18, 20])

'''

'''
A = 1.0
f_0 = 10**5
omega_0 = 2 * np.pi * f_0
phi = np.pi / 8 
