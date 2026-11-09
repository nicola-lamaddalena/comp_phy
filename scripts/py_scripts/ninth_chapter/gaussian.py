import numpy as np
import matplotlib.pyplot as plt

# BOX-MULLER METHOD FOR GAUSSIAN DISTRIBUTION
sigma = 1.0
def box_muller(z: float) -> tuple[float, float]:
    theta = np.random.uniform() * 2 * np.pi
    r = np.sqrt(-2 * sigma**2 * np.log(1 - z))
    x, y = r * np.cos(theta), r * np.sin(theta)

    return x, y

xs, ys = [], []
for _ in range(10000):
    z = np.random.uniform()
    x, y = box_muller(z)
    xs.append(x)
    xs.append(y)

pdf_xs = []
for x in xs:
    pdf_xs.append(np.exp(-x**2 / 2*sigma**2) / np.sqrt(2 * np.pi * sigma**2))

plt.plot(xs, pdf_xs, "ro")
plt.hist(xs, bins=50, density=True)
plt.show()
