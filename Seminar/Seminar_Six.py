####1.Вводится список целых чисел в одну строчку через пробел.
####Необходимо оставить в нем только двузначные числа.
####Реализовать программу с использованием функции filter.
####Результат отобразить на экране в виде последовательности
####оставшихся чисел в одну строчку через пробел.
##
##
##nums = list(map(int,input('Введите').split()))
##print(nums)
##num = list(filter(lambda x: 9< x < 100, nums))
##string = ''
##for i, item in enumerate(num):
##    string += str(item) + ' '
##
##print(string)
##
##nuw_nums = [n for n in nums if n%2 == 0]
##
##print(nuw_nums)

##Решение преподавателя
##print(*filter(lambda x: len(str(abs(int(x)))) == 2, input().split()))


####2. Дан список, вывести отдельно буквы и цифры.
##
##list_user = ['f', 'r', 'w', 1, 4, 5, 6]
##char = [n for n in list_user if type(n) == str]
##print(char)
##
##num = [n for n in list_user if type(n) == int]
##print(num)


####3. Преобразовать набора списков
####users = ['user1','user2','user3','user4','user5']
####ids = [4, 5, 9, 14, 7]
####salary = [111,222,333]
####в другой набор
####
####['user1', 4, 111]
####['user2', 5, 222]
####['user3', 9, 333]
####
####и потом вернуть в исходное состояние
####
####['user1', 'user2', 'user3']
####[4, 5, 9]
####[111, 222, 333]
##
##users = ['user1','user2','user3','user4','user5']
##ids = [4, 5, 9, 14, 7]
##salary = [111,222,333]
##
##res = list(zip(users, ids, salary))
##for i, item in enumerate(res):
##    print(list(item))
##
##print(res)
##
##new_users = []
##new_ids = []
##new_salary = []
##
##
##for i, item in enumerate(res):
##    for j, itn in enumerate(item):
##        if j == 0:
##            new_users.append(itn)
##        elif j == 1:
##            new_ids.append(itn)
##        else:
##            new_salary.append(itn)
##
##print(new_users)
##print(new_ids)
##print(new_salary)

## Решение преподавателя
users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]

a,b,c = map(list,zip(users, ids, salary))
print(a,b,c, sep="\n")
a,b,c= map(list,zip(a,b,c))

print(a,b,c, sep="\n")


