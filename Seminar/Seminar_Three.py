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

# Орел и решка
#
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
#
# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
#
# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.
#
# Примечание. Если выпавших Решек нет, то необходимо вывести число
# 0
# 0.
#
# Тестовые данные 🟢
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3
# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7
# Sample Input 3:
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3:
# 31
#
# str = input('Введите строку: ')
#
# count = 0
# mas = []
# for s in str:
#     if s == 'Р':
#         count += 1
#     else:
#         count = 0
#
#     mas.append(count)
#
# print(f'Наибольшее количество подряд выпавших Решек: {max(mas)}')

# # решение преподавателя
# s = input()
# t = 0
# while "Р" * (t + 1) in s:
#     t += 1
#     if t != 0:
#         print(t)
#     else:
#         print(0)


# ///////////////////////////////////////////////////////////////////////////////////////////
# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
#
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие
# последовательности букв), то холодильник заражен и нужно вывести номер холодильника,
# нумерация начинается с единицы
#
# Формат входных данных
# В первой строке подаётся число
# n
# n – количество холодильников. В последующих
# n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от
# 5
# 5 до
# 100
# 100 символов.
#
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел.
# Если таких холодильников нет, ничего выводить не нужно.
#
# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8
#
# # Создаем пустой словарь
# dict_holod = {}
#
# # Пользовательский ввод и заполнения словаря
# key_user = int(input('Введите количество холодильников: '))
# for count in range(key_user):
#     dict_holod[count] = input(f'Введите строку с данными для холодильника {count + 1}: ')
#
# # print(dict_holod)
#
# # Проверяем заражен ли холодильник
# # Порядковый номер холодильника
# numbers_hol = 1
#
# # Переменная для хранения номеров зараженных холодильников
# result = ''
#
# # Цикл поиска зараженных холодильников
# for values in dict_holod.values():
#     str_hol = values
#     string = ''
#     for s in str_hol:
#         if s == 'a':
#             string = s
#         elif s == 'n' and string == 'a':
#             string += s
#         elif s == 't' and string == 'an':
#             string += s
#         elif s == 'o' and string == 'ant':
#             string += s
#         elif s == 'n' and string == 'anto':
#             string += s
#
#     # Если холодильник заражен то вносим его в номер в result
#     if string == 'anton':
#         result = result + ' ' + str(numbers_hol)
#
#     numbers_hol += 1
#
# # Вывод результата
# print(f'Номера зараженных холодильников:{result}')


# //////////////////////////////////////////////////////////////////
# # Задача с предиктатами
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(not (x or y or z) == (not x and not y and not z))


# ///////////////////////////////////////////////////////////////////////////////////////////
# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
string = ['tyh', 1, 'yuj', 4, 'etr']
number = int(input('Введите число для поиска в строке:'))

if number in string:
    print("Yes")
else:
    print('No')
