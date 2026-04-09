import numpy as np
import matplotlib.pyplot as plt

'''
Plan is to implement the entire Task 1 and 2 here, by calling other functions
'''
from src.FFT import fft
def MLE(z):
    
    w = np.array([10 ** i for i in range(20)])
    F = np.array([fft(z, w[i]) for i in range(20)])
    plt.plot(w, np.real(F))
    plt.plot(w, np.imag(F))
    plt.show()


    k = [10, 12, 14, 16, 18, 20]
     

    return (None, None)


from src.sample import Z
from src.FFT import fft, phi_hat


def wrap_to_pi(angle):
    return (angle + np.pi) % (2 * np.pi) - np.pi


def MLE(mc_runs=MC_RUNS):
    """
    FFT-based MLE simulation for task 1a.

    Returns
    -------
    results : dict
        results[M] is a dict containing:
            "snr_db"      : array of SNR values in dB
            "var_omega"   : variance of omega estimation error
            "var_phi"     : variance of phase estimation error
            "mean_omega"  : mean omega estimation error
            "mean_phi"    : mean phase estimation error
    """
    results = {}

    for M in FFT_SIZES:
        var_omega = []
        var_phi = []
        mean_omega = []
        mean_phi = []

        for sigma, snr_db in zip(SIGMA_SNR, SNR_DECIBEL):
            omega_errors = np.zeros(mc_runs)
            phi_errors = np.zeros(mc_runs)

            for k in range(mc_runs):
                z = Z(sigma=sigma)
                z = np.asarray(z).flatten()

                omega_hat, _, _ = fft(z, M)
                phase_hat = phi_hat(z, omega_hat)

                omega_errors[k] = omega_0 - omega_hat
                phi_errors[k] = wrap_to_pi(phi - phase_hat)

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
