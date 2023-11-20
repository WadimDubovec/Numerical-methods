def gauss_method(matrix, vector):
    n = len(matrix)

    # Вывод исходной системы уравнений
    print("Исходная система уравнений:")
    for i in range(n):
        print(matrix[i], "|", vector[i])

    # Прямой ход метода Гаусса
    for i in range(n):
        max_el = abs(matrix[i][i])
        max_row = i
        for k in range(i + 1, n):
            # Поиск максимального элемента в столбце
            if abs(matrix[k][i]) > max_el:
                max_el = abs(matrix[k][i])
                max_row = k

        # Обмен строк, если необходимо
        if max_row != i:
            print("\nШаг", i + 1, ": Обмен строкой", i + 1, "со строкой", max_row + 1)
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            vector[i], vector[max_row] = vector[max_row], vector[i]

            # Вывод матрицы после обмена
            print("Матрица после обмена:")
            for j in range(n):
                print(matrix[j], "|", vector[j])

        # Проверка, что элемент на главной диагонали не равен 0
        if matrix[i][i] == 0:
            print("\nЭлемент на главной диагонали равен 0. Решений нет.")
            return

        # Деление строки на первый элемент строки
        divisor = matrix[i][i]
        matrix[i] = [elem / divisor for elem in matrix[i]]
        vector[i] /= divisor


        # Вычитание строк
        for k in range(i + 1, n):
            c = -matrix[k][i]
            matrix[k] = [elem + c * matrix[i][j] for j, elem in enumerate(matrix[k])]
            vector[k] += c * vector[i]

        # Вывод матрицы после прямого хода
        print("\nШаг", i + 2, ": Делим строку", i + 1, "на", divisor)
        print("Матрица после деления и вычитания:")
        for j in range(n):
            print(matrix[j], "|", vector[j])

    print('\n' + '#' * 50)

    # Обратный ход метода Гаусса
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = vector[i]
        print(f"\nШаг {n - i}: x[{i}] = {x[i]}")
        for k in range(i + 1, n):
            x[i] -= matrix[i][k] * x[k]
            print(f"Вычитаем {matrix[i][k]} * {x[k]} =", matrix[i][k] * x[k])
        print(f"Итого: x[{i}] =", x[i])

    # Вывод решения системы уравнений
    print("\nРешение системы уравнений:")
    for i in range(n):
        print(f"x[{i}] =", x[i])


def main():
    print("Выберите способ ввода чисел:")
    print("1. Конкретные числа")
    print("2. С клавиатуры")
    print("3. Через переменные уравнения")

    choice = int(input("Введите номер выбранного способа: "))

    if choice == 1:
        # Заданные матрица и вектор
        A = [
            [2.3, 5.7, -0.8],
            [3.5, -2.7, 5.3],
            [1.7, 2.3, -1.8]
        ]

        b = [-6.49, 19.2, -5.09]

        gauss_method(A, b)
    elif choice == 2:
        # Ввод матрицы и вектора с клавиатуры
        n = int(input("Введите размерность системы уравнений (n): "))
        A = []
        b = []

        print("Введите коэффициенты матрицы:")
        for i in range(n):
            row = []
            for j in range(n):
                element = float(input(f"Введите коэффициент A[{i + 1}][{j + 1}]: "))
                row.append(element)
            A.append(row)

        print("Введите коэффициенты вектора b:")
        for i in range(n):
            element = float(input(f"Введите коэффициент b[{i + 1}]: "))
            b.append(element)

        gauss_method(A, b)
    elif choice == 3:
        # Ввод переменных уравнения
        # Пользователь вводит a1, a2, a3
        a1 = int(input("Введите a1:"))
        a2 = int(input("Введите a2:"))
        a3 = int(input("Введите a3:"))

        A = [
            [2*a1 + 4*a2, 2*(a1 - a2), 2*(a1 - a2)],
            [2*(a1 - a2), 2*a1 + a2 + 3*a3, 2*a1 + a2 - 3*a3],
            [2*(a1 - a2), 2*a1 + a2 - 3*a3, 2*a1 + a2 + 3*a3]
        ]

        b = [-4*a1 - 2*a2, -4*a1 + a2 + 9*a3, -4*a1 + a2 - 9*a3]

        gauss_method(A, b)
    else:
        print("Некорректный выбор. Завершение программы.")

    print(f"\n{'#'*50}\nВектор невязки:")


if __name__ == "__main__":
    main()


