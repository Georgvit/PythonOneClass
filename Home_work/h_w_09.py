# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# Пользовательский ввод
number_n = int(input('Введите число N '))

# Создание списка элементов
list_number = list(range(-number_n, number_n + 1))

# Изначальное значение произведения
multi = 1

# Чтение индексов из файла и вычисление произведения
with open('file_index.txt', 'r') as file:
    line_in_file = file.readline()
    while line_in_file:
        multi = multi * list_number[int(line_in_file)]
        line_in_file = file.readline()

#  Вывод результата
print(f'Произведение элементов на указанных позициях: {multi}')
