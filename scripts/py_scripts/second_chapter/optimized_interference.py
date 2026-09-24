import numpy as np
import matplotlib.pyplot as plt

ROW_LEN = 1024
LAM = 15
K = 2 * np.pi / LAM
AMPLITUDE = 10

sources = np.array([
    [512, 412],
    [512, 612],
])

# Separazione automatica di coordinate X e Y per tutte le sorgenti
sources_x = sources[:, 0]
sources_y = sources[:, 1]

x = np.arange(0, ROW_LEN)
y = np.arange(0, ROW_LEN)
X, Y = np.meshgrid(x, y, indexing='ij')

# Calcolo adattivo indipendente dal numero di sorgenti
dx = X[:, :, np.newaxis] - sources_x  # Forma: (256, 256, N_sources)
dy = Y[:, :, np.newaxis] - sources_y  # Forma: (256, 256, N_sources)
R = np.sqrt(dx**2 + dy**2)

# La somma lungo axis=2 somma automaticamente tutte le N sorgenti presenti
LATTICE = np.sum(AMPLITUDE * np.sin(K * R), axis=2)

plt.imshow(LATTICE, origin="lower")
plt.show()
