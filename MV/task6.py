import numpy as np


def SetArr(v, n):
    array = np.zeros((n, n + 1), dtype=float)
    array.reshape(n, n + 1)
    # for i in range(n):
    #   array[i] = [0] * (n + 1)
    for i in range(n):
        for j in range(n):
            if i == j:
                array[i][j] = v + 2 * i
            else:
                array[i][j] = (v + 2 * i) * 0.01  # 2-10 строка - ввод А
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += (v + 2 * j) * array[i][j]
        array[i][n] = round(sum, 2)  # 14-18 строка - ввод столбца b
    return array


def Gauss(array):
    import copy
    import numpy as np

    def SetArr(v, n):
        array = np.zeros((n, n + 1), dtype=float)
        array.reshape(n, n + 1)
        # for i in range(n):
        #   array[i] = [0] * (n + 1)
        for i in range(n):
            for j in range(n):
                if i == j:
                    array[i][j] = v + i
                else:
                    array[i][j] = (v + i) * 0.01  # 2-10 строка - ввод А
        for i in range(n):
            sum = 0
            for j in range(n):
                sum += (v + j) * array[i][j]
            array[i][n] = round(sum, 2)  # 14-18 строка - ввод столбца b
        return array

    def Gauss(array):
        print("Р.М.К.:")
        # showA(array)

        for i in range(len(array)):  # прямой ход
            divideStr(array, i)
            for j in range(i + 1, len(array)):
                minusStrs(array, i, j)
        print("Прямой ход:")
        # showA(array)

        for i in range(len(array) - 1, -1, -1):  # НОВЫЙ обратный ход
            for j in range(i - 1, -1, -1):
                minusStrs3(array, i, j)
        print("НОВЫЙ Обратный ход:")
        # showA(array)

        otv = [0] * len(array)
        otv = np.zeros(len(array), dtype=float)
        for i in range(len(array)):
            otv[i] = array[i][-1]
        print(f"Ответ: {otv}")
        return otv

    def showA(array):
        for i in range(0, len(array)):  # Вывод А
            for j in range(0, len(array[i])):
                print(f"{round(array[i][j], 4)}\t", end="")
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

    # Gauss(6, 5)

    def setArray(n):
        array = [0] * n
        for i in range(n):
            array[i] = [0] * (n)
        return array

    def Prilojenie_k_mGaussa(array):
        arraycopy = copy.deepcopy(array)
        # arraycopy.extend(array)
        dividers = [0] * len(array)
        for i in range(len(array)):  # прямой ход
            divideStrPriloj(array, i, dividers)
            for j in range(i + 1, len(array)):
                minusStrs(array, i, j)
        for i in range(len(array)):  # занулить последний столбец
            array[i][-1] = 0
        print("Прямой ход:")
        showA(array)

        opredelitel = 1
        for el in dividers:
            opredelitel *= el
        print(f"Определитель: {opredelitel}")

        otv = [0] * len(array)
        arraycopy2 = copy.deepcopy(arraycopy)
        for i in range(len(arraycopy2)):
            arraycopy2[i][-1] = 1
            otv[i] = Gauss(arraycopy2)
            arraycopy2 = copy.deepcopy(arraycopy)
        print("OTV")
        showA(otv)
        otv2 = np.array(otv, dtype=float)
        otv2.transpose()
        showA(otv2)
        print("умн а а-1")
        otv_NP = np.array(otv, dtype=float)
        array1 = np.array([[3, 6, -1], [4, 2, 3], [1, -4, -2]], dtype=float)
        w = np.linalg.inv(array1)

        c = np.dot(otv_NP, array1)
        print("обр мат")
        showA(w)
        return otv

    def divideStrPriloj(array, i, dividers):
        if array[i][i] == 0:
            pvge(array, i)
        divider = array[i][i]
        dividers[i] = divider
        for j in range(i, len(array[i])):
            array[i][j] /= divider

    array = np.array([[3, 6, -1, 0], [4, 2, 3, 0], [1, -4, -2, 0]], dtype=float)

    Prilojenie_k_mGaussa(array)

    array = np.array([[-3, 1, 3, 4, 0], [3, 0, -1, 4, 0], [-5, 2, 3, 0, 0], [4, -1, 2, -6, 0]], dtype=float)

    Prilojenie_k_mGaussa(array)
    # otv = Gauss(SetArr(6, 5))
    # for el in otv:
    # print(el)
    # array = [[1, 2, 3, 4, 5], [1, 1, -1, 2, 3], [1, 1, -1, 2, 3], [1, 2, -2, 4, 6]]
    # Gauss(array)


def showA(array):
    for i in range(0, len(array)):  # Вывод А
        for j in range(0, len(array[i])):
            print(f"{round(array[i][j],4)}\t", end="")
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


# SetArr(6,3)
#Gauss(SetArr(2, 5))
