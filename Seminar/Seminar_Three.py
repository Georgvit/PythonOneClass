# Лекция два
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.write('\nLINE12\n')
# data.write('LINE31\n')
# data.close()

# # Конструкция with
# with open('file.txt', 'a') as data:
#     data.write('line 11\n')
#     data.write('line 12\n')


# exit()
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# /////////////////////////////////////////////////////////////////
# Функции

# import Seminar_One as number_function
# print(number_function.f(1))

# def new_string(symbol, count=3):
#     return symbol * count
#
#
# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(4))

# def concatenatio(*params):
#     res: str = ""
#     for iten in params:
#         res += iten
#     return res
#
#
# print(concatenatio('a', 's', 'e', 't'))
# print(concatenatio('3', 't'))

# /////////////////////////////////////////////////////////////////////////
# Рекурсия

# Фибоначи
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# Кортежи - не изменяемый список

# a = (3, 4, 5, 8)
# # print(a)
# # print(a[0])
# # print(a[1])
#
# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'black'])
# red, green, black = t
# print('r:{} g:{} b:{}'.format(red, green, black))

# Словари

# # Заполняем пустой словарь
# dict = {}
# dict = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
#
# print(dict)
# print(dict['right'])
#
# for k in dict.keys():
#     print(k)
#
# for i in dict.items():
#     print(i)
#
# for v in dict.values():
#     print(v)

# Множества
# colors = {'red', 'green', 'blue'}
# print(type(colors))
# print(colors)
#
# colors.add('grey')
# print(colors)
#
# colors.remove('red')
# print(colors)
#
# colors.discard('green')
# print(colors)
#
# colors.clear()
# print(colors)
#
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# print(c)
#
# u = a.union(b)
# print(u)
#
# i = a.intersection(b)
# print(i)
#
# dl = a.difference(b)
# print(dl)
#
# dr = b.difference(a)
# print(dr)
#
#
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
#
# print(q)
#
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b)

# # Списки
#
# list1 = [1, 2, 3, 4, 5]
# list2 = list1
#
# list1[0] = 123
# list1[1] = 333
#
# for e in list1:
#     print(e)
#
# print()
#
# for e in list2:
#     print(e)
#
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
#
# list1.append(45)
# print(list1)
# list1.insert(1, 11)
# print(list1)
# list1.insert(2, 12)
# print(list1)

# ///////////////////////////////////////////////////////////////////////////////////////////
# Семинар ТРИ