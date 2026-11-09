import numpy as np
import matplotlib.pyplot as plt

def f(x: float, t: float) -> float:
    return -x**3 + np.sin(t)

a, b = 0.0, 10.0
x0 = 0.0
hs = [0.01, 0.1, 0.2, 0.5, 1.0]

for h in hs:
    ts = np.arange(a, b, h)
    x = x0
    xs = []
    for t in ts:
        xs.append(x)
        k1 = h * f(x, t)
        k2 = h * f(x + k1/2, t + h/2)
        k3 = h * f(x + k2/2, t + h/2)
        k4 = h * f(x + k3, t + h)
        x += (k1 + 2*k2 + 2*k3 + k4) / 6
    plt.plot(ts, xs, label=f"h = {h}")

plt.xlabel(r"$t$")
plt.ylabel(r"$x(t)$")
plt.legend()
plt.show()
