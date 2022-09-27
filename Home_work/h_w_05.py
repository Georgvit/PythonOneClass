# Напишите программу, которая принимает на вход координаты
#  двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# Пользовательский ввод координат
print('Введите координаты точки А')
coordinate_point_ax = int(input('Введите X: '))
coordinate_point_ay = int(input('Введите Y: '))

print('Введите координаты точки Б')
coordinate_point_bx = int(input('Введите X: '))
coordinate_point_by = int(input('Введите Y: '))

# Вычисляем  расстояние между точками А и Б

disstance = (((coordinate_point_ax - coordinate_point_bx)**2) + ((coordinate_point_ay - coordinate_point_by) ** 2))**0.5
print(round(disstance,2))