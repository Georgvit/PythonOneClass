# Реализуйте алгоритм перемешивания списка.

import random

# Пользовательский ввод


def input_user():
    number_n = int(input('Введите количество элементов в списке: '))
    return number_n

# Создание случайного списка


def random_list(input_user):
    count = 0
    random_list = []
    while count < input_user:
        random_list.append(random.randint(-100, 100))
        count += 1

    print(f'Оригинальный список: {random_list}')
    return random_list

# Метод перемешивания списка


def mixing(random_list):

    # Первый метод
    random.shuffle(random_list)
    print(f'Перемешивание списка методом shuffle: {random_list}')

# Второй метод
    list_length = len(random_list)
    for count in range(list_length):
        # Получение случайного индекса
        index_aleatory = random.randint(0, list_length - 1)
        # Замена
        temp = random_list[count]
        random_list[count] = random_list[index_aleatory]
        random_list[index_aleatory] = temp

    print(f'Перемешивание списка через цикл for:  {random_list}')


#  Вызов методов
mixing(random_list(input_user()))
