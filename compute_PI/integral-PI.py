import numpy as np
from test_PI import test_PI

# Compute the integral of 4 * sqrt(1-x^2) from 0 to 1. It should return PI.
def integral_PI():
    n = 1000000
    x = np.random.uniform(0, 1, n)
    y = 4 * np.sqrt(1 - x**2)
    pi = np.mean(y)
    test_PI(pi)
    return pi

integral_PI()
