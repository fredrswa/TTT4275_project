import matplotlib.pyplot as plt


def plot_task1_results(results, crb_omega, crb_phi):
    """
    Plot task 1a results:
    - variance of frequency estimation error vs SNR
    - variance of phase estimation error vs SNR

    Parameters
    ----------
    results : dict
        Output from MLE().
        results[M] contains:
            "snr_db", "var_omega", "var_phi", ...
    crb_omega : np.ndarray
        CRLB for omega variance across SNR.
    crb_phi : np.ndarray
        CRLB for phi variance across SNR.
    """
    # Use any one entry to get the common SNR axis
    first_M = next(iter(results))
    snr_db = results[first_M]["snr_db"]

    # Frequency plot
    plt.figure()
    plt.semilogy(snr_db, crb_omega, "k--", linewidth=2, label="CRLB")

    for M, data in results.items():
        plt.semilogy(data["snr_db"], data["var_omega"], marker="o", label=f"M = {M}")

    plt.xlabel("SNR [dB]")
    plt.ylabel(r"Var$(\omega_0 - \hat{\omega})$")
    plt.title("Frequency estimation variance vs SNR")
    plt.grid(True, which="both")
    plt.legend()

    # Phase plot
    plt.figure()
    plt.semilogy(snr_db, crb_phi, "k--", linewidth=2, label="CRLB")

    for M, data in results.items():
        plt.semilogy(data["snr_db"], data["var_phi"], marker="o", label=f"M = {M}")

    plt.xlabel("SNR [dB]")
    plt.ylabel(r"Var$(\phi - \hat{\phi})$")
    plt.title("Phase estimation variance vs SNR")
    plt.grid(True, which="both")
    plt.legend()

    plt.show()
