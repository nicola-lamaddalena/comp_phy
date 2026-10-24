import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt

def buckingham(x: np.float64) -> np.float64:
    sigma = 10e-9
    return (sigma/x)**6 - np.exp(-x / sigma)

x = 0.5

def gradient(x1: np.float64, x2: np.float64, gammas: npt.NDArray[np.float64], f: callable) -> np.float64:
    eps = 10e-9
    x3s = []
    for gamma in gammas:
        x3 = x2 - gamma * (f(x1) - f(x2)) / (x1 - x2)
        x3s.append(x3)

    return x3s

gammas = np.linspace(1, 10, 10)
plt.plot(np.array(gradient(0.5, 5, gammas, buckingham)))
plt.show()
