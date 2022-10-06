# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.


# Если в задаче имелось ввиду создать список в котором элементы не повторяются
# Пользовательский ввод
# number_list = input('Задайте последовательность чисел через пробел\n и нажмите ввод: ').split()
# Преобразование строковых данных в тип int
# number_list = [int(x) for x in number_list]
#
# print(f'Введенная последовательность: {number_list}')
# Сортировка введенной последовательности
# number_list.sort()
#
# Создание нового списка
# sort_number_list = []
# length_list = len(number_list) - 1

# Выборка
# for i in range(length_list):
#     if number_list[i] != number_list[i + 1]:
#         sort_number_list.append(number_list[i])
#
# if (sort_number_list[len(sort_number_list) - 1]) != number_list[len(number_list) - 1]:
#     sort_number_list.append(number_list[len(number_list) - 1])
#
# Вывод результата
# print(f'Список из неповторяющихся элементов: {sort_number_list}')


# Если в задаче имелось ввиду создать список в который вносятся элементы НЕ повторяющиеся в оригинальном списке
# Пользовательский ввод
number_list = input('Задайте последовательность чисел через пробел\n и нажмите ввод: ').split()
# Преобразование строковых данных в тип int
number_list = [int(x) for x in number_list]

print(f'Введенная последовательность: {number_list}')
# Сортировка введенной последовательности
number_list.sort()

# Создание нового списка
sort_number_list = []

# Выборка
for i in range(len(number_list)):
    count = 0
    for j in range(len(number_list)):
        if number_list[i] == number_list[j]:
            count += 1
    if count == 1:
        sort_number_list.append(number_list[i])


# Вывод результата
print(f'Список из неповторяющихся элементов: {sort_number_list}')
