import numpy as np
import numpy as np
import matplotlib.pyplot as plt

from src.sample import X_sampled
from src.tests import run_tests
from src.CRB import CRB
from src.MLE import MLE


def main():
    #run_tests() 
    n0 = 100
    N = 1/(1**6) * 100000
    X_sam = X_sampled(n0, N)



    (w_hat_CRB, phi_hat_CRB) = CRB(X_sam, n0, N)

    (w_hat_MLE, phi_hat_MLE) = MLE(X_sam, n0, N)
    return None





if __name__ == "__main__":
    main()
