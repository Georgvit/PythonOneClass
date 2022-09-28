# Задайте список из n чисел последовательности (1 + 1/n)^n
#  и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# Пользовательский ввод
def input_user():
    number_n = int(input('Введите число N: '))
    return number_n


# Создание словаря
def number_dictionary(key_dictionary):
    count = 1
    dictionary = {}
    while count <= key_dictionary:
        dictionary[count] = (round((1 + 1 / count) ** count, 2))
        count += 1

    print(dictionary)


# Запуск методов
number_dictionary(input_user())
