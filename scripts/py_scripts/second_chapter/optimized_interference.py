import numpy as np
import matplotlib.pyplot as plt

ROW_LEN = 2048
LAM = 50
K = 2 * np.pi / LAM
AMPLITUDE = 1

sources = np.array([
    [ROW_LEN/2, ROW_LEN/2 - ROW_LEN/10],
    [ROW_LEN/2, ROW_LEN/2 + ROW_LEN/10],
])

# Separazione automatica di coordinate X e Y per tutte le sorgenti
sources_x = sources[:, 0]
sources_y = sources[:, 1]

x = np.arange(0, ROW_LEN)
y = np.arange(0, ROW_LEN)
X, Y = np.meshgrid(x, y, indexing='ij')

# Calcolo adattivo indipendente dal numero di sorgenti
dx = X[:, :, np.newaxis] - sources_x  # Forma: (ROW_LEN, ROW_LEN, N_sources)
dy = Y[:, :, np.newaxis] - sources_y  # Forma: (ROW_LEN, ROW_LEN, N_sources)
R = np.sqrt(dx**2 + dy**2)

# La somma lungo axis=2 somma automaticamente tutte le N sorgenti presenti
LATTICE = np.sum(AMPLITUDE * np.sin(K * R), axis=2)

plt.imshow(LATTICE, origin="lower")
plt.inferno()
plt.show()
