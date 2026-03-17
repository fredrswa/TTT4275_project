import numpy as np
import numpy as np
import matplotlib.pyplot as plt


from src.sample import Z
from src.tests import run_tests
from src.CRB import CRB
from src.MLE import MLE

import constants

def main():
    #run_tests() 
    #Get Z, which is the sampled values of X(t)
    z = Z()

    (w_hat_CRB, phi_hat_CRB) = CRB(z)
    print(f"{(w_hat_CRB, phi_hat_CRB)=}")

    (w_hat_MLE, phi_hat_MLE) = MLE(z)
    print(f"{(w_hat_MLE, phi_hat_MLE)=}")

    
    return None





if __name__ == "__main__":
    main()
