import numpy as np


from constants import SIGMA_SNR, T, N, P, Q, n0


def CRB():
    sigma = SIGMA_SNR
    var_omega_hat = 12 * sigma ** 2 / (T**2 * N*(N**2 - 1))
    var_phi_hat   = 12 * sigma ** 2 * (N * n0**2 + 2 * n0 * P + Q) / (N**2 * (N**2 - 1)) 
    return (var_omega_hat, var_phi_hat)
