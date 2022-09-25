# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# print('введиет число А')
# number_one = int(input())

# print('введиет число Б')
# number_two = int(input())

# if (number_one == (number_two * number_two)):
#     print('Число А является квадратом числа Б')
# elif(number_two == (number_one * number_one)):
#     print('Число Б является квадратом числа А')
# else:
#     print('Числа не являются квадратами другруга')


# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# print('Введите числа массива')
# list = input().split()

# list = [int(item) for item in list]

# print('Массив')
# print(list)

# print('Максимальное число')
# print(max(list))

# max_number = 0
# count = 0
# while count < len(list):
#     if (max_number < list[count]):
#         max_number = list[count]
#     count += 1

# print('Максимальное число вторым способом')
# print(max_number)


# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# *Примеры:*

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# number_n = int(input('Введите число N '))
# number_rev = -number_n
# while number_rev <= number_n:
#     print(number_rev)
#     number_rev += 1

# Второй вариант
# for i in range(number_rev, number_n + 1):
#     print(i, end= " ")

# Третий вариант
# print(list(range(-number_n, number_n +1)))


# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# number_n = float(input('Введите число N '))

# if (int(number_n * 10 % 10) > 0):
#     print(int(number_n * 10 % 10))
# elif (int(number_n * 10 % 10) < 0):
#     print(int(number_n * -10 % 10))
# else:
#     print('Нет')


# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# number_n = int(input('Введите число N '))
# border_lower = 5
# border_upper = 30

# while (border_upper > border_lower):
#     if (border_lower != border_upper - 10):
#         if (number_n % border_lower == 0):
#             print('Число кратно ', border_lower)
#             border_lower += 5
#         else:
#             print('Число не кратно ', border_lower)
#             border_lower += 5
#     else:
#         break
