# sum = lambda x: x + 10
# mult = lambda x: x ** 2
# print(sum(mult(2)))
#
# sum1 = lambda x: x + 22
# mult2 = lambda x: x ** 3
# print(sum1(mult2(2)))
#
# sum4 = lambda x: x + 242
# mult4 = lambda x: x ** 5
# print(sum4(mult2(2)))


# def sum(x, y):
#     return x + y
#
#
# # Тоже самое что запись выше
# func = lambda x, y: x + y
#
#
# def mylt(x, y):
#     return x * y
#
#
# def calc(op, a, b):
#     print(op(a, b))
#     return op(a, b)
#
#
# calc(func, 4, 5)

# list = []
#
# for i in range(1, 21):
#     if i % 2 == 0:
#         list.append(i)
# print(list)

# То же самое
# # Список
# list = [i for i in range(1, 22) if i % 2 == 0]
# print(list)

# # Кортежи
# list = [(i, i) for i in range(1, 22) if i % 2 == 0]
# print(list)

# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# # Мое решение
# def f(x):
#     return x ** 2
#
#
# file_us = [1, 2, 3, 5, 8, 15, 23, 38]
#
# list = [(i, f(i)) for i in (file_us) if i % 2 == 0]
# print(list)

# # Решение преподавателя
# f = open('f.txt', 'r')
# data = f.read() + ' '
# f.close()
# numbers = []
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
#
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
#
# print(out)

# # Реление с lambda
#
# def select(f, col):
#     return [f(x) for x in col]
#
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
#
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)

# Функция map

# li = [x for x in range(1, 20)]
# # Преобразуем полученый список с помощью map
# li = list(map(lambda x: x + 10, li))
# print(li)

# # Ввод чисел с преобразованием в лист
# data = list(map(int, input().split(',')))
# print(data)

# data = list(map(int, input().split(',')))
#
# for e in data:
#     print(e)

# # Версия с map and filter
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# # ZIP
# # Функция zip() применяется к набору итерируемых
# # объектов и возвращает итератор с кортежами из
# # элементов входных данных
#
# user = ['user1', 'user2', 'user3', 'user4']
# isd = [4, 5, 6, 7, 9]
# salary = [111, 222, 444]
#
# data = list(zip(user, isd, salary))
# print(data)
#
# # Функция enumerate() применяется к итерируемому
# # объекту и возвращает новый итератор с кортежами
# # из индекса и элементов входных данных
#
# user = ['user1', 'user2', 'user3', 'user4']
# isd = [4, 5, 6, 7, 9]
# salary = [111, 222, 444]
#
# data = list(enumerate(user))
# print(data)
