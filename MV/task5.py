import numpy
import scipy.interpolate
x = [int(xn) for xn in input().split()]
f = [int(fn) for fn in input().split()]
h=1
matrix = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, f[0]],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, f[1]],
          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, f[2]],
          [1, h, h**2, h**3, 0, 0, 0, 0, 0, 0, 0, 0, f[1]],
          [0, 1, 0, 0, 1, h, h**2, h**3, 0, 0, 0, 0, f[2]],
          [0, 0, 1, 0, 0, 0, 0, 0, 1, h, h**2, h**3, f[3]],
          [0, 1, 2*h, 3*h**2, 0, -1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 2*h, 3*h**2, 0, -1, 0, 0, 0, 0],
          [0, 0, 2, 6*h, 0, 0, -2, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 2, 6*h, 0, 0, -2, 0, 0],
          [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 6 * h, 0],
         ]
for i in range(len(matrix)):
    print(matrix[i])
