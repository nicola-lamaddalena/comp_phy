import time
import numpy as np
import matplotlib.pyplot as plt

C, N, m, k, omega = 1, 100, 1, 6, 2
alpha = 2 * k - m * omega ** 2

def linsolve_gaussian(A: np.array, v: np.array) -> np.array:
    N = len(v)
    for m in range(N):
        pivot_row = m + np.argmax(np.abs(A[m:, m]))
        if pivot_row != m:
            A[[m, pivot_row]] = A[[pivot_row, m]]
            v[[m, pivot_row]] = v[[pivot_row, m]]

        div = A[m, m]
        if abs(div) < 1e-15:
            raise ZeroDivisionError("Matrix is singular/nearly singular: no usable pivot")

        A[m, :] /= div
        v[m] /= div

        for i in range(m + 1, N):
            mult = A[i, m]
            A[i, :] -= mult * A[m, :]
            v[i] -= mult * v[m]

    x = np.empty(N, float)
    for m in range(N - 1, -1, -1):
        x[m] = v[m]
        for i in range(m + 1, N):
            x[m] -= A[m, i] * x[i]
    return x

def linsolve_tridiag(A, v) -> np.array:
    N = len(v)
    for i in range(N - 1):
        A[i, i + 1] /= A[i, i]
        v[i] /= A[i, i]
        A[i + 1, i + 1] -= A[i + 1, i] * A[i, i + 1]
        v[i + 1] -= A[i + 1, i] * v[i]
    v[N - 1] /= A[N - 1, N - 1]

    x = np.empty(N, float)
    x[N - 1] = v[N - 1]
    for i in range(N - 2, -1, -1):
        x[i] = v[i] - A[i, i + 1] * x[i + 1]
    return x

A = np.zeros([N,N], float)
for i in range(N - 1):
    A[i, i] = alpha
    A[i, i + 1] = A[i + 1, i] = -k
A[0, 0] = A[N - 1, N - 1] = alpha - k
v = np.zeros(N, float)
v[0] = C

start = time.perf_counter()
x1 = linsolve_tridiag(A, v)
print(f"Time elapsed for x1: {time.perf_counter() - start}")
plt.plot(x1, "-ro")
plt.show()

