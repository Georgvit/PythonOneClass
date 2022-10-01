# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Пользовательский ввод
number_dec = int(input('Введите десятичное число: '))

# Перевод в двоичную систему и запись во временную переменную
temporary_variable = []
while number_dec != 0:
    temporary_variable.append(number_dec % 2)
    number_dec //= 2

temporary_variable.reverse()

# Вывод двоичного числа
binary_number = ''
for i in range(len(temporary_variable)):
    binary_number = binary_number + str(temporary_variable[i])

print(f'Двоичное число: {binary_number}')
