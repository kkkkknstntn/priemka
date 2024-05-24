def inverse_matrix_gauss(A):
    A_extended = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(A)]

    # Прямой ход метода Гаусса
    for col in range(n):
        max_val = abs(A_extended[col][col])
        max_row = col
        for k in range(col + 1, n):
            if abs(A_extended[k][col]) > max_val:
                max_val = abs(A_extended[k][col])
                max_row = k
        # Переставляем строки
        A_extended[col], A_extended[max_row] = A_extended[max_row], A_extended[col]

        # Проходим по столбцам и обнуляем нижние элементы
        for k in range(col + 1, n):
            factor = A_extended[k][col] / A_extended[col][col]
            for j in range(col, 2 * n):
                A_extended[k][j] -= factor * A_extended[col][j]

    # Обратный ход метода Гаусса
    for i in range(n - 1, -1, -1):
        divisor = A_extended[i][i]
        for j in range(i, 2 * n):
            A_extended[i][j] /= divisor

        for k in range(i - 1, -1, -1):
            factor = A_extended[k][i]
            for j in range(i, 2 * n):
                A_extended[k][j] -= factor * A_extended[i][j]

    A_inv = [row[n:] for row in A_extended]
    return A_inv


n= int(input('dim = '))
matr = [[-3, 1, 3, 4], [3, 0, -1, 4], [-5, 2, 3, 0], [4, -1, 2, -6]]
print(*matr, sep='\n')
print()
print(*inverse_matrix_gauss(matr), sep='\n')