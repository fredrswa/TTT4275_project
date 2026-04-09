import numpy as np
import matplotlib.pyplot as plt


import constants
from src.sample import Z
from src.tests import run_tests
from src.CRB import CRB
from src.MLE import MLE

def main():
    #Get Z, which is the sampled values of X(t)
    (w_hat_CRB, phi_hat_CRB) = CRB()
    print(f"{(w_hat_CRB, phi_hat_CRB)=}")

    results = MLE()
    print(results)

if __name__ == "__main__":
    main()
