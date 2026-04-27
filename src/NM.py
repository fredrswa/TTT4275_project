import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

from src.sample import Z
from src.FFT import fft, phi_hat

from constants import FFT_SIZES, SIGMA_SNR, SNR_DECIBEL, omega_0, phi, n0, T, N

def wrap_to_pi(angle):
    return (angle + np.pi) % (2 * np.pi) - np.pi

def neg_log_likelihood(theta, z):
    omega, phase = theta

    n = n0 + N - 1
    t = np.arange(n0*T, n*T, T)

    x_hat = np.exp(1j * (omega * t + phase))

    return np.sum(np.abs(z - x_hat) ** 2)


def NM():
    mc_runs = 1000
    M = FFT_SIZES[0]

    var_omega   = []
    var_phi     = []
    mean_omega  = []
    mean_phi    = []
    success_rate= []

    for sigma, snr_db in zip(SIGMA_SNR, SNR_DECIBEL):
        omega_errors = np.zeros(mc_runs)
        phi_errors   = np.zeros(mc_runs)
        successes = 0
        for k in range(mc_runs):
            z = Z(sigma=sigma)
            z = np.asarray(z).flatten()

            omega_hat_init, _, _    = fft(z, M)
            phase_hat_init          = phi_hat(z, omega_hat_init)

            res = minimize(
                neg_log_likelihood, 
                x0=np.array([omega_hat_init, phase_hat_init]),
                args=z,
                method="Nelder-Mead",
                options={"maxiter": 1200, "xatol"  : 1e-10, "fatol"  : 1e-10},
            )
            omega_hat, phi_hat_ = res.x
            omega_errors[k]     = omega_0 - omega_hat
            phi_errors[k]       = wrap_to_pi(phi - phi_hat_)
            if res.success == 1:
                successes +=1

        var_omega.append(np.var(omega_errors, ddof=1))
        var_phi.append(np.var(phi_errors, ddof=1))
        mean_omega.append(np.mean(omega_errors))
        mean_phi.append(np.mean(phi_errors))
        success_rate.append(successes/mc_runs)

    results = {
            "snr_db": np.array(SNR_DECIBEL),
            "var_omega": np.array(var_omega),
            "var_phi": np.array(var_phi),
            "mean_omega": np.array(mean_omega),
            "mean_phi": np.array(mean_phi),
            "success_rate": np.array(success_rate)
    }
    return results
