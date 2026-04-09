import numpy as np
import matplotlib.pyplot as plt


import constants
from src.sample import Z
from src.tests import run_tests
from src.CRB import CRB
from src.MLE import MLE

def main():
    #Get Z, which is the sampled values of X(t)
    z = Z()
    print(constants.SNR_DECIBEL)
    print(constants.SNR_LINEAR)
    print(constants.SIGMA_SNR)
    (w_hat_CRB, phi_hat_CRB) = CRB()
    print(f"{(w_hat_CRB, phi_hat_CRB)=}")

    (w_hat_MLE, phi_hat_MLE) = MLE(z)
    print(f"{(w_hat_MLE, phi_hat_MLE)=}")


if __name__ == "__main__":
    main()
