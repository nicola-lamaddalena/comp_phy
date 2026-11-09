import numpy as np
import matplotlib.pyplot as plt

x0, xf = 0, 2
N = 10_000

def f(x: float) -> float:
    return np.sin(1 / (x * (2 - x)))**2

xin, yin = [], []
xout, yout = [], []
k = 0
for _ in range(N):
    x = 2 * np.random.uniform(x0, xf)
    y = np.random.uniform(0, 1)
    if y < f(x):
        xin.append(x)
        yin.append(y)
        k += 1
    else:
        xout.append(x)
        yout.append(y)

I = k * 2 / N
print(I)

xs = np.linspace(x0 + 0.001, xf - 0.001, N)
plt.plot(xs, f(xs))
plt.scatter(xin, yin, c="green")
plt.scatter(xout, yout, c="blue")
plt.show()
