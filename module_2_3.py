# Исходный список
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Начальный индекс
index = 0

# Цикл while для перебора списка
while index < len(my_list):
    # Если текущее число отрицательное, прерываем цикл
    if my_list[index] < 0:
        break
    # Если положительное число, выводим его на консоль
    if my_list[index] > 0:
        print(my_list[index])

    # Переходим к следующему элементу списка
    index += 1