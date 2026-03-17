import numpy as np


from constants import SIGMA_I, SIGMA_R, P, Q, N, T, n0



def CRB(x_sam):
    
    sigma = SIGMA_R + 1j * SIGMA_I


    var_omega_hat = 12 * sigma ** 2 / (T**2 * N*(N**2 - 1))
    var_phi_hat   = 12 * sigma ** 2 * (N * n0**2 + 2 * n0 * P + Q) / (N**2 * (N**2 - 1)) 

    return (var_omega_hat, var_phi_hat)
