
import numpy as np
import matplotlib.pyplot as plt

import sys

y0 = 0
yN = 1
h = 0.01


def Gauss(a):
    n = len(a)
    x = np.zeros(n)
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')

        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]

        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]
    return x


lambda_ = 1
X = np.arange(y0 + h / 2, yN - h / 2, h, dtype=np.float_)
n = len(X)


def A(x: np.float_, t: np.float_) -> np.float_:
    return x * t + x ** 2 * t ** 2 + x ** 3 * t ** 3
def f(x: np.float_) -> np.float_:
    return 2 * (4 / 3 * x + 1 / 4 * x ** 2 + 1 / 5 * x ** 3)


M = np.zeros([n - 1, n], dtype=np.float_)

for i in range(n - 1):
    for j in range(n - 1):
        M[i][j] = lambda_ * h * A(X[i], X[j])
        if i == j:
            M[i][j] += 1
    M[i][n - 1] = f(X[i])

np.set_printoptions(precision=6, linewidth=100, suppress=True)


def y_true(x: np.float_) -> np.float_:
    return 2 * x

Y_res = np.array(Gauss(M), dtype=np.float_)
Y_actual = np.zeros(len(X), dtype=np.float_)
for i in range(len(X)):
    Y_actual[i] = y_true(X[i])
Eps = abs(Y_actual[:-1] - Y_res)
print(Y_res )
print()
print(Y_actual)
print()
print(Eps )
