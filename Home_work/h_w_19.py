# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

# number_list = input('Задайте последовательность чисел через пробел\n и нажмите ввод: ').split()
# number_list = [int(x) for x in number_list]
#
# print(f'Введенная последовательность: {number_list}')
# number_list.sort()
#
# sort_number_list = []
# length_list = len(number_list) - 1
#
# for i in range(length_list):
#     if number_list[i] != number_list[i + 1]:
#         sort_number_list.append(number_list[i])
#
# if (sort_number_list[len(sort_number_list) - 1]) != number_list[len(number_list) - 1]:
#     sort_number_list.append(number_list[len(number_list) - 1])
#
# print(f'Список неповторяющихся элементов: {sort_number_list}')

number_list = input('Задайте последовательность чисел через пробел\n и нажмите ввод: ').split()
number_list = [int(x) for x in number_list]

print(f'Введенная последовательность: {number_list}')
number_list.sort()

sort_number_list = []
leng = len(number_list) - 1
count = 0
while count > leng:
    if number_list[count] == number_list[count + 1]:
        del number_list[count:count+1]


print(number_list)