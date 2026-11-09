import numpy as np
import matplotlib.pyplot as plt

sigma, rho, beta = 10, 28, 8/3
t0, t = 0, 50
x0, y0, z0 = 0, 1, 0

def f(x: float, y: float, z: float, t: float) -> tuple[float, float, float]:
    fx = sigma * (y - x)
    fy = rho * x - y - x * z
    fz = x * y - beta * z
    return (fx, fy, fz)

hs = [0.01, 0.1, 0.2, 0.5, 1.0]

for h in hs:
    ts = np.arange(t0, t, h)
    x, y, z = x0, y0, z0
    xs = []
    ys = []
    zs = []
    for t in ts:
        xs.append(x)
        ys.append(y)
        zs.append(z)
        fx, fy, fz = f(x, y, z, t)
        k1x, k1y, k1z = h * fx, h * fy, h * fz
        k2x, k2y, k2z = h * f(x + k1x/2, y + k1y/2, z + k1z/2, t + h/2)
        k3x, k3y, k3z = h * f(x + k1x/2, y + k1y/2, z + k1z/2, t + h/2)
        k4x, k4y, k4z = h * f(x + k3x, y + k3y, z + k3y, t + h)
        x += (k1x + 2*k2x + 2*k3x + k4x) / 6
        y += (k1y + 2*k2y + 2*k3y + k4y) / 6
        z += (k1z + 2*k2z + 2*k3z + k4z) / 6
    plt.plot(ts, xs, label=f"h = {h}")
    plt.plot(ts, ys, label=f"h = {h}")
    plt.plot(ts, zs, label=f"h = {h}")

plt.xlabel(r"$t$")
plt.ylabel(r"$x(t)$")
plt.legend()
plt.show()
