# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# Функция фибоначи

def Fibonacci(number):
    if number < 0:
        if number == -1 or number == -2:
            return -1
        else:
            return -(Fibonacci(-number - 2) + Fibonacci(-number - 1))
    if number == 0:
        return 0
    if number > 0:
        if number == 1 or number == 2:
            return 1
        else:
            return Fibonacci(number - 2) + Fibonacci(number - 1)


# Пользовательский ввод
user_name = int(input('Введите число для построения списка чисел Фибоначи: '))

# Переменная для записи результата
result = []

# Вызов функции
count = -user_name
while count < user_name + 1:
    result.append(Fibonacci(count))
    count += 1

# Вывод результата
print(f'Список чисел Фибоначчи: {result}')
