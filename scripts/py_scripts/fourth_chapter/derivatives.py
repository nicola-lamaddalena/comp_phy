import numpy as np
import matplotlib.pyplot as plt

h1, h2 = 0.1, 0.01
x1, x2 = -2, 2
def f(x: float) -> float:
    return 1 + np.tanh(2*x)/2

def f_prime(points: np.array) -> float:
    return 1 / np.cosh(2 * points)**2

points1 = np.linspace(-2, 2, int((x2-x1)/h1))
points2 = np.linspace(-2, 2, int((x2-x1)/h2))

def fd(points: np.array, h: float) -> float:
    return (f(points + h) - f(points)) / h

def cd(points: np.array, h: float) -> float:
    return (f(points + h) - f(points - h)) / (2 * h)

fig, ax = plt.subplots(2, 1)
ax[0].plot(f_prime(points1), "x", label="analytical")
ax[0].plot(fd(points1, h1), "x", label="fd")
ax[0].plot(cd(points1, h1), label="cd")
ax[1].plot(f_prime(points2), "x", label="analytical")
ax[1].plot(fd(points2, h2), "x", label="fd")
ax[1].plot(cd(points2, h2), label="cd")
plt.legend()
plt.show()

x0 = 0.5
hs = np.array([10**(-k) for k in range(1, 17)])
print(hs)
fd_h = abs(f_prime(x0) - fd(x0, hs))
cd_h = abs(f_prime(x0) - cd(x0, hs))
print(fd_h, cd_h)
plt.loglog(hs, fd_h, "-o", label="fd error")
plt.loglog(hs, cd_h, "-o", label="cd error")
plt.legend()
plt.show()
