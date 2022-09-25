# print ('Hello World!!!')
# print ('Я инженер')

# типы данных
# int, float, boolean, str, list, None

# a = 123
# b = 1.23

#value = None
# print(type (value))

# print(type (a))
# print(type (b))

#value = 123456

#print(type (value))

#s = 'hello \n world'
# s = 'hello world'
# print(s)

# print (a,'-', b,'-', s)
# print ('{2} - {1} - {0}'. format(a, b, s))
# print (f'{a} - {b} - {s}')

# f = True
# print (f)

# list = [1, 2, 3]
# print(list)

# listOne = ['1', '2', '3', 'hello']
# print(listOne)

# print('ввведите a')
# a = int(input())

# print('ввведите b')
# b = int(input())

# print('{} {}'.format(a, b))
# print(f'{a} {b}')
# print('Сумма a + b =', a + b)

# Арифметические операции
# Важно и нужно, без них вы не напишете ни одной
# программы
# Если помните математику – проблем не будет
# +, - , * , / , % , // , **
# Приоритет операций
# ** , ⊕, ⊖, * , /, //, %, +, -
# ( ) Скобки меняют приоритет

# a = 123
# b = -321
# c = a + b
# print(c)


# a = 12
# b = 21
# c = a * b
# print(c)

# Получам число с запятой
# a = 3
# b = 32
# c = a / b
# print(c)

# Получаем целое число
# a = 32
# b = 3
# c = a // b
# print(c)

# Степень
# a = 32
# b = 3
# c = a ** b
# print(c)

# a = 3.2123
# b = 3
# c = round(a * b, 3)
# print(c)

# iter = 2
# iter += 3  # iter = iter + 3
# iter -= 4  # iter = iter - 4
# iter *= 5  # iter = iter * 5
# iter /= 5  # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5  # iter = iter % 5
# iter **= 5 # iter = iter ** 5
# print(iter)

# ЛОГИЧЕСКИЕ ОПЕРАЦИИ

# Логические операции
# > , >= , < , <= , == , !=
# not, and, or – не путать с & , | , ^
# Кое-что ещё: is, is not, in, not in

# a = [1, 2]
# b = [1, 2]
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# a = 1 < 3 < 5 > 10
# print(a)

# func = 1
# T = 4
# x = 3
# print(func<T>x)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)

# #Проверка на четность
# is_odd = not f[0] % 2

# print(is_odd)

# a = int (input('a = '))
# b = int (input('b = '))

# if a > b:
#     print('max ', a)
# else:
#     print('max ', b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# for i in 1, -2, 3, 14, 5:
#     print(i)

# list = [1, 2, 3, 7, 90]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)


# for i in range(1, 10, 2):
#     print(i)

# Немного о строках

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#  print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# Списки

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# Функции
# def f(x):
#     return x**2

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# arg = 2.3
# print(f(arg))
# print(type(f(arg)))

value = 'Hexlet'
print(value)
# Пропускаем обе границы
value[::-1]  
# 'telxeH'
print(value[::-1])