import numpy as np
import matplotlib.pyplot as plt
import cmath

from src.function import X



def plot_signal():
    print("Running tests")
    Fs = 10 ** 7
    t = np.arange(0, 0.0001, 1/Fs)
    X_real = np.real(X(t))
    X_imag = np.imag(X(t))
    plt.plot(t, X_real)
    #plt.plot(t, X_imag)

    plt.show()

def run_tests():
    plot_signal()
