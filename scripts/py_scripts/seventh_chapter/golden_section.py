import numpy as np
import matplotlib.pyplot as plt

z = 1.618
x1, x4 = 0.5, 5
x2 = x4 - (x4 - x1) / z
x3 = x1 + (x4 - x1) / z

def golden_search(x1: np.float64, x4: np.float64, x2: np.float64, x3: np.float64, f: callable) -> np.float64:
    eps = 10e-6
    if (x4 - x1) > eps:
        if f(x2) < f(x3):
            x4 = x3
            x3 = x2
            x2 = x4 - (x4 - x1) / z
            return golden_search(x1, x4, x2, x3, f)
        else:
            x1 = x2
            x2 = x3
            x3 = x1 + (x4 - x1) / z
            return golden_search(x1, x4, x2, x3, f)
    else:
        return (x1 + x4) / 2

def buckingham(x: np.float64) -> np.float64:
    sigma = 1
    return ((sigma / x)**6 - np.exp(-x / sigma))

print(golden_search(x1, x4, x2, x3, buckingham))
