import numpy as np
import matplotlib.pyplot as plt
import cmath

from src.function import X



def run_tests():
    print("Running tests")
    t = np.arange(0, 100, 0.1)
    plt.plot(t, X(t))
    plt.show()


