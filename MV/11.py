import numpy as np


def SetArr(v, n):
    array = np.zeros((n, n + 1), dtype=float)
    array.reshape(n, n + 1)
    # for i in range(n):
    #   array[i] = [0] * (n + 1)
    array[0][0]= 1 + 1/3
    array[0][1] = 1/4
    array[0][2] = 1/5
    array[1][0] = 1 / 4
    array[1][1] = 1 + 1 / 5
    array[1][2] = 1 / 6
    array[2][0] = 1 / 5
    array[2][1] = 1 / 6
    array[2][2] = 1 + 1 / 7
    array[0][3] = 1969/3600 * v
    array[1][3] = 5/12 * v
    array[2][3] = 283/840 * v

    return array


def Gauss(array):

   # showA(array)

    for i in range(len(array)):  # прямой ход
        divideStr(array, i)
        for j in range(i + 1, len(array)):
            minusStrs(array, i, j)


    for i in range(len(array) - 1, -1, -1):  # НОВЫЙ обратный ход
        for j in range(i - 1, -1, -1):
            minusStrs3(array, i, j)

   # showA(array)

    otv = [0] * len(array)
    otv = np.zeros(len(array), dtype=float)
    for i in range(len(array)):
        otv[i] = array[i][-1]
  #  print(f"Ответ: {otv}")
    return otv


def showA(array):
    for i in range(0, len(array)):  # Вывод А
        for j in range(0, len(array[i])):
            print(f"{round(array[i][j],15)}\t", end="")
        print()
    print()


def divideStr(array, i):
    if array[i][i] == 0:
        pvge(array, i)
    diviver = array[i][i]
    for j in range(i, len(array[i])):
        array[i][j] /= diviver


def pvge(array, i):
    st_max = i + np.argmax(array[i:, i])

    if array[i][st_max] != 0:
        array[[i, st_max]] = array[[st_max, i]]
        return
    stolb_max = i + np.argmax(array[i, i:-1])

    array[:, [i, stolb_max]] = array[:, [stolb_max, i]]
    return


def minusStrs(array, i, j):
    multiplier = array[j][i]
    for k in range(i, len(array[i])):
        array[j][k] -= array[i][k] * multiplier


def minusStrs3(array, i, j):  # ИЗ J ВЫЧЕСТЬ I УМН НА A[J][I]
    multiplier = array[j][i]
    for k in range(len(array[j]) - 1, i - 1, -1):
        array[j][k] -= array[i][k] * multiplier

def y(x):
    a = Gauss(SetArr(2, 3))
    s=0
    for i in range (3):
        s += (a[i]*(x**(i+1)))

    return (2 * (4/3*x + 1/4 * x*x +1/5 *x*x*x )- s*1)

x1 = [0.2, 0.3, 0.6, 0.8]
y1 = [0, 0,0,0]
y2 = [0,0,0,0]
e=[0,0,0,0]
for i in range(4):
    y1[i] = y(x1[i])
    y2[i] = 2 *x1[i]
    e[i] = y1[i] - y2[i]

(x1)
print(*y1)
print(*y2)
print(*e)
# SetArr(6,3)

