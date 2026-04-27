import matplotlib.pyplot as plt

def plot_task1a_results(results, crb_omega, crb_phi):
    first_M = next(iter(results))
    snr_db = results[first_M]["snr_db"]

    plt.figure()
    plt.semilogy(snr_db, crb_omega, "k--", linewidth=2, label="CRLB")

    for M, data in results.items():
        plt.semilogy(data["snr_db"], data["var_omega"], marker="o", label=f"M = {M}")

    plt.xlabel("SNR [dB]")
    plt.ylabel(r"Var$(\omega_0 - \hat{\omega})$")
    plt.title("Frequency estimation variance vs SNR")
    plt.grid(True, which="both")
    plt.legend()

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


def plot_task1b_results(results_nm, crb_omega, crb_phi):
    snr_db = results_nm["snr_db"]

    plt.figure()
    plt.semilogy(snr_db, crb_omega, "k--", linewidth=2, label="CRLB")
    plt.semilogy(
        snr_db,
        results_nm["var_omega"],
        marker="o",
        label="Nelder-Mead refined MLE",
    )

    plt.xlabel("SNR [dB]")
    plt.ylabel(r"Var$(\omega_0 - \hat{\omega})$")
    plt.title("Task 1b: NM frequency estimation variance vs SNR")
    plt.grid(True, which="both")
    plt.legend()

    plt.figure()
    plt.semilogy(snr_db, crb_phi, "k--", linewidth=2, label="CRLB")
    plt.semilogy(
        snr_db,
        results_nm["var_phi"],
        marker="o",
        label="Nelder-Mead refined MLE",
    )

    plt.xlabel("SNR [dB]")
    plt.ylabel(r"Var$(\phi - \hat{\phi})$")
    plt.title("Task 1b: NM phase estimation variance vs SNR")
    plt.grid(True, which="both")
    plt.legend()

    plt.figure()
    plt.plot(snr_db, results_nm["success_rate"], marker="o")
    plt.xlabel("SNR [dB]")
    plt.ylabel("Optimizer success rate")
    plt.title("Task 1b: Nelder-Mead convergence rate")
    plt.grid(True)

    plt.show()
