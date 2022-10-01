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

# Создаем пустой словарь
dict_fridge = {}

# Пользовательский ввод и заполнение словаря
key_user = int(input('Введите количество холодильников: '))
for count in range(key_user):
    dict_fridge[count] = input(f'Введите строку с данными для холодильника {count + 1}: ')

# print(dict_holod)

# Проверяем заражен ли холодильник
# Порядковый номер холодильника
numbers_fridge = 1

# Переменная для хранения номеров зараженных холодильников
result = ''

# Или создаем список для хранения
result_list = []

# Цикл поиска зараженных холодильников
for values in dict_fridge.values():
    str_hol = values
    string = ''
    for s in str_hol:
        if s == 'a':
            string = s
        elif s == 'n' and string == 'a':
            string += s
        elif s == 't' and string == 'an':
            string += s
        elif s == 'o' and string == 'ant':
            string += s
        elif s == 'n' and string == 'anto':
            string += s

    # Если холодильник заражен то вносим его в номер в result
    if string == 'anton':
        result = result + ' ' + str(numbers_fridge)
        result_list.append(numbers_fridge)

    numbers_fridge += 1

# Вывод результата
print(f'Номера зараженных холодильников:{result}')
print(f'Номера зараженных холодильников:{result_list}')
