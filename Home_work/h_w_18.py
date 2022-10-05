# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# Пользовательский ввод
user_number = int(input('Введите натуральное число N: '))

# Список натуральных простых множителей
prime_factors = \
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
     47, 53, 59, 31, 67, 71, 73, 79, 83, 89, 97, 101, 103,
     107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
     167, 173, 179, 181, 191, 193, 197, 199]

# Поиск натуральных множителей для заданного числа
count = 0
list_divider = []
while user_number > 1:
    if ((user_number / prime_factors[count]) - int(user_number / prime_factors[count])) == 0:
        user_number = user_number / prime_factors[count]
        list_divider.append(prime_factors[count])
    elif ((user_number / prime_factors[count]) - int(user_number / prime_factors[count])) != 0:
        count += 1

# Вывод результата
print(f'Простые множители для вашего числа: {list_divider}')