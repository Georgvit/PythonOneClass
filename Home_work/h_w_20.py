#Задана натуральная степень k.
#Сформировать случайным образом список коэффициентов
#(значения от 0 до 100) многочлена и записать в файл многочлен степени k.

#Пример:

#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

#Пользовательский ввод
degree_k = int(input('Введите натуральную степень многочлена: '))

#Функция получения рандомного значения коэффциентов
def ration():
    ratio_n = random.randint(0, 100)
    return ratio_n

#Функция вызова многочлена
def fun():
    polynomial = 'x^'
    return polynomial
text_file = open('text_file.txt','w+')

#Вывод многочлена
result_function = ''
while degree_k != 0:
    if degree_k == 1:
        if result_function == '':
            result_function = str(ration()) + '*x'
            text = (f'{result_function} = 0\n')
            text_file.write(text)
            print(f'{result_function} = 0')
            text = (f'{result_function} + {ration()} = 0\n')
            text_file.write(text)
            print(f'{result_function} + {ration()} = 0')
            degree_k = int(degree_k) - 1
        else:
            result_function = result_function + ' + ' + str(ration()) + '*x'
            text = (f'{result_function} + {ration()} = 0\n')
            text_file.write(text)
            print(f'{result_function} + {ration()} = 0')
            degree_k = int(degree_k) - 1
    elif degree_k > 1:
        if result_function == '':
            result_function =  result_function + str(ration()) + '*' + fun() + str(degree_k)
            text = (f'{result_function} = 0\n')
            text_file.write(text)
            print(f'{result_function} = 0')
            text = (f'{result_function} + {ration()} = 0\n')
            text_file.write(text)
            print(f'{result_function} + {ration()} = 0')
            degree_k = int(degree_k) - 1
        else:
            result_function =  result_function + ' + ' + str(ration()) + '*' + fun() + str(degree_k)
            text = (f'{result_function} + {ration()} = 0\n')
            text_file.write(text)
            print(f'{result_function} + {ration()} = 0')
            degree_k = int(degree_k) - 1

print('Все данные записаны в файл text_file.txt')
text_file.seek(0)
text_file.close()