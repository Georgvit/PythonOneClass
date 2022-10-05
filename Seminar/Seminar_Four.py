# # Больше предыдущего
# # На вход программе подается строка текста из натуральных чисел.
# # Из неё формируется список чисел. Напишите программу подсчета количества чисел,
# # которые больше предшествующего им в этом списке числа, то есть, стоят вслед за меньшим числом.
# # Формат входных данных
# # На вход программе подается строка текста из разделенных пробелами натуральных чисел.
# # Формат выходных данных
# # Программа должна вывести одно число – количество элементов списка, больших предыдущего.
#
# # Тестовые данные 🟢
# # Sample Input 1:
# # 1 2 3 4 5
# # Sample Output 1:
# # 4
# # Sample Input 2:
# # 1 1 3 2 2 1 1 1 1
# # Sample Output 2:
# # 1
# # Sample Input 3:
# # 5 4 3 2 1
# # Sample Output 3:
# # 0
#
# # Ввод строки от пользователя
# string = input('Введите строку для анализа: ')
# string = string.replace(' ', '')
# count = 0
# number_of_numbers = 0
#
# # Цикл анализа
# for count in range(len(string) - 1):
#     if int(string[count]) < int(string[count + 1]):
#         number_of_numbers += 1
#
#     count += 1
#
# # Вывод результата
# print(f'Количество чисел,которые больше предшествующего: {number_of_numbers}')


# # Написать программу для транслитерации
# # 'a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z',
# # 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r',
# # 's', 't', 'u', 'f', 'kh', 'ts', 'ch',
# # 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya'
#
# string_text = input('Введите текс для транслитерации: ')
#
#
# en = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z',
# 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r',
# 's', 't', 'u', 'f', 'kh', 'ts', 'ch',
# 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya', ' ', ',', '.', '!', '?']
#
# ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з',
# 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
# 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
# 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', ',', '.', '!', '?']
#
#
#
# new_string_text = ''
# for count in range(len(string_text)):
#         index = ru.index(string_text[count].lower())
#         if string_text[count].isupper():
#             char = string_text[count].replace(string_text[count], en[index].upper())
#             new_string_text = new_string_text + char
#         else:
#             char = string_text[count].replace(string_text[count], en[index])
#             new_string_text = new_string_text + char
#
# print(new_string_text)

# ГЕНИАЛЬНОЕ РЕШЕНИЕ В ГРУППЕ
# transleterate = \
# {'а': 'a','б': 'b','в': 'v','г' : 'g','д' : 'd','е' : 'e','ж' : 'zh','з' : 'z','и' : 'i',
# 'й' : 'y','к' : 'k','л' : 'l','м' : 'm','н' : 'n','о' :'o','п' : 'p','р' : 'r','с' : 's',
# 'т' : 't','у' : 'u','ф' : 'f','х' : 'kh','ц' : 'ts','ч' : 'ch','ш' : 'sh','щ' : 'shch',
# 'ь' : '\'','ы' :'y','ъ' : '','э' : 'e','ю' : 'yu','я' : 'ya'}
# text = input('input: ')
#
# for i in text:
# print(transleterate[i], end = "")

# Решение преподавателя
t = \
    ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o',
     'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

start_index = ord('а')
title = 'Переводим этот текст, сейчас!'
print(title.lower())

slug = ""
for s in title.lower():
    if "а" <= s <= "я":
        slug += t[ord(s) - ord('а')]
        print(ord(s), ord('а'))
    else:
        slug += s

print(slug)
