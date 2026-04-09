
import numpy as np

from constants import T, N, n0


def F(z, w):    
    z = np.asarray(z).flatten()
    n = np.arange(N)
    return np.sum(z * np.exp(-1j * w * n * T)) / N

def fft(z, M):
    Z_fft = np.fft.fft(z, n=M)
    m_star = np.argmax(np.abs(Z_fft))
    omega_hat = 2 * np.pi * m_star / (M * T)

    return omega_hat, m_star, Z_fft

def phi_hat(z, omega_hat):
    N = np.size(z)
    n = np.arange(N) + n0
    F_hat = np.mean(z * np.exp(-1j * omega_hat * n * T))
    phi_hat = np.angle(F_hat)
    return phi_hat
