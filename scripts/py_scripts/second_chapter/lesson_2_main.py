import numpy as np
import matplotlib.pyplot as plt

ROW_LEN = 256
X1, Y1 = 128, 0
X2, Y2 = 100, 0
X3, Y3 = 156, 0
X4, Y4 = 70, 0
X5, Y5 = 186, 0
LAM = 5
K = 2 * np.pi / LAM
AMPLITUDE = 1
LATTICE = np.zeros((ROW_LEN, ROW_LEN))

def wave(x: float, y: float, center_x: float, center_y: float) -> float:
    r = np.sqrt((center_x - x)**2 + (center_y - y)**2)
    return AMPLITUDE * np.sin(K * r)

pos_x = np.arange(0, ROW_LEN, 1)
pos_y = np.arange(0, ROW_LEN, 1)

for i in range(len(pos_x)):
    for j in range(len(pos_y)):
        w1 = wave(pos_x[i], pos_y[j], X1, Y1)
        w2 = wave(pos_x[i], pos_y[j], X2, Y2)
        w3 = wave(pos_x[i], pos_y[j], X3, Y3)
        w4 = wave(pos_x[i], pos_y[j], X4, Y4)
        w5 = wave(pos_x[i], pos_y[j], X5, Y5)
        LATTICE[i,j] = (w1 + w2 + w3 + w4 + w5)

plt.imshow(LATTICE, origin="lower")
plt.show()
