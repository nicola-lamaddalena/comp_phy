import numpy as np
import matplotlib.pyplot as plt

accuracy = 1e-12
initial, final = -0.99, 0.99
N = 100

def arctan(u):
    x = 0
    delta = 1

    while (np.max(np.abs(delta)) - accuracy) > 0:
        delta = (np.tanh(x) - u) * np.cosh(x)**2
        x -= delta

    return x

us = np.linspace(initial, final, N)
xs = arctan(us)

plt.plot(xs)
plt.show()
