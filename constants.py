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
SIGMA_R = 0.1
SIGMA_I = 0.1
SNR_DECIBEL = np.array([-10 + i * 10 for i in range(8)])
SNR_LINEAR  = 10**(SNR_DECIBEL/10)
SIGMA_SNR = np.sqrt(1 / (2 * SNR_LINEAR))

'''
FFT
'''
FFT_SIZES = np.array([10, 12, 14, 16, 18, 20]) ** 2

