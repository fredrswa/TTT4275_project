import numpy as np
import matplotlib.pyplot as plt
from src.sample import Z
from src.FFT import fft, phi_hat

from constants import FFT_SIZES, SIGMA_SNR, SNR_DECIBEL, omega_0, phi
'''
Plan is to implement the entire Task 1 and 2 here, by calling other functions
'''
def wrap_to_pi(angle):
    return (angle + np.pi) % (2 * np.pi) - np.pi

def MLE():
    results = {}
    mc_runs = 1
    for M in FFT_SIZES:
        var_omega   = []
        var_phi     = []
        mean_omega  = []
        mean_phi    = []

        for sigma, snr_db in zip(SIGMA_SNR, SNR_DECIBEL):
            omega_errors = np.zeros(mc_runs)
            phi_errors   = np.zeros(mc_runs)

            for k in range(mc_runs):
                z = Z(sigma=sigma)
                z = np.asarray(z).flatten()

                omega_hat, _, _     = fft(z, M)
                phase_hat           = phi_hat(z, omega_hat)
                omega_errors[k]     = omega_0 - omega_hat
                phi_errors[k]       = wrap_to_pi(phi - phase_hat)

            var_omega.append(np.var(omega_errors, ddof=1))
            var_phi.append(np.var(phi_errors, ddof=1))
            mean_omega.append(np.mean(omega_errors))
            mean_phi.append(np.mean(phi_errors))

        results[M] = {
            "snr_db": np.array(SNR_DECIBEL),
            "var_omega": np.array(var_omega),
            "var_phi": np.array(var_phi),
            "mean_omega": np.array(mean_omega),
            "mean_phi": np.array(mean_phi),
        }
    return results
