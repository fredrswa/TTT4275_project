
import numpy as np
import cmath

from constants import A, omega_0, phi


def X(t):
    return A * np.exp((omega_0 * t + phi)*1j)
