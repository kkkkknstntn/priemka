import numpy as np

def SetArr(v, n):
    array = np.zeros((n, n + 1), dtype=float)
    array.reshape(n, n + 1)
    for i in range(n):
        array[i] = [0] * (n + 1)
    for i in range(n):
        for j in range(n):
            if i == j:
                array[i][j] = v + 2 * i
            if j - 1 == i or j + 1 == i:
                array[i][j] = (v + 2 * i) * 0.01  # 2-10 строка - ввод А
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += (v + 2 * j) * array[i][j]
        array[i][n] = round(sum, 2)  # 14-18 строка - ввод столбца b
    return array

# Вывод матрицы на экран
def print_arr(string, namevec, a):
    if (type(a) == int) or (type(a) == float):
        print(a)
    else:
        print(string)
        for k in range(len(a)):
            print("{}[{}] = {:8.4f}".format(namevec, k, a[k]))

# Процедура нахождения решения 3-х диагональной матрицы
def solution(a):
    n = len(a)
    x = [0 for k in range(0, n)]  # обнуление вектора решений
    print('Размерность матрицы: ', n, 'x', n)

    # Прямой ход
    v = [0 for k in range(0, n)]
    u = [0 for k in range(0, n)]
    # для первой 0-й строки
    v[0] = a[0][1] / (-a[0][0])
    u[0] = (- a[0][n]) / (-a[0][0])
    for i in range(1, n - 1):  # заполняем за исключением 1-й и (n-1)-й строк матрицы
        v[i] = a[i][i + 1] / (-a[i][i] - a[i][i - 1] * v[i - 1])
        u[i] = (a[i][i - 1] * u[i - 1] - a[i][n]) / (-a[i][i] - a[i][i - 1] * v[i - 1])
    # для последней (n-1)-й строки
    v[n - 1] = 0
    u[n - 1] = (a[n - 1][n - 2] * u[n - 2] - a[n - 1][n]) / (-a[n - 1][n - 1] - a[n - 1][n - 2] * v[n - 2])
    # Обратный ход
    x[n - 1] = u[n - 1]
    for i in range(n - 1, 0, -1):
        x[i - 1] = v[i - 1] * x[i] + u[i - 1]

    return x


# MAIN - блок программмы
x = solution(SetArr(2,5))  # Вызываем процедуру решение
print_arr('Решение: ', 'x', x)
