# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# Пользовательский ввод
user_in = input('Введите число: ')

# Подсчет суммы цифр в числе
sum = 0
count = 0

while count < len(user_in):
    if '-' == user_in[count]:
         count += 1
    elif '.' != user_in[count]:
        sum = sum + int(user_in[count])
        count += 1
    else:
        count += 1

# Вывод результата
print(f'Сумма цифр числа: {sum}')
