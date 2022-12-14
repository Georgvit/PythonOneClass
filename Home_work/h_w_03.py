# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# Пользовательский ввод координат
coordinate_x = int(input('Введите координату Х: '))
coordinate_y = int(input('Введите координату Y: '))

# Вычисляем номер плоскости координатной сетки

if coordinate_x > 0 and coordinate_y > 0:
    print("Номер плоскости координатной сетки - 1")
elif coordinate_x < 0 and coordinate_y > 0:
    print("Номер плоскости координатной сетки - 2")
elif coordinate_x < 0 and coordinate_y < 0:
    print("Номер плоскости координатной сетки - 3")
elif coordinate_x > 0 and coordinate_y < 0:
    print("Номер плоскости координатной сетки - 4")
else:
    print("Координаты 0-0")