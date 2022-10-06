# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов

# Создаем и открываем файлы для записи многочленов
list_one_file = open('one_text_polynomial.txt', 'w+')
list_two_file = open('two_text_polynomial.txt', 'w+')

# В данной версии программы работа возможна только с многочленами с одинаковым количеством
# элементов.
# Записываем данные в файл и закрываем их
list_one_file.write('2*x^2 + 4*x + 5*a + 6*b')
list_two_file.write('4*x^2 + 4*x^3 + 5*a + 6*b')
list_one_file.close()
list_two_file.close()

# Открываем файлы для чтения данных
with open('one_text_polynomial.txt', 'r') as file:
    list_one = file.readlines()

with open('two_text_polynomial.txt', 'r') as file:
    list_two = file.readlines()

# Переводим в строковый формат
list_one = ''.join(list_one)
list_two = ''.join(list_two)

# Вывод результата считывания
print(f'Первый многочлен: {list_one}')
print(f'Второй многочлен: {list_two}')

# Подготовка строк
list_one = list_one.split(' + ')
list_two = list_two.split(' + ')

if len(list_one) >= len(list_two):
    length_list = len(list_one) - 1
else:
    length_list = len(list_two) - 1

result = ''

# Сложение многочленов
for i in range(length_list):
    element_a = list_one[i].split('*')
    element_b = list_two[i].split('*')
    if element_a[1] == element_b[1]:
        result = result + ' + ' + str(int(element_a[0]) + int(element_b[0])) + '*' + element_a[1]
    elif element_a[1] != element_b[1]:
        result = result + ' + ' + element_a[0] + element_a[1] + ' + ' + element_b[0] + element_b[1]

# Вывод результата
print(f"Сумма многочленов: {result.partition('+ ')[-1]}")
