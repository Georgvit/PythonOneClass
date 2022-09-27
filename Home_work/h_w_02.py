# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


list_xyz = ["X", "Y", "Z"]
list = []
for i in range(3):
    list.append(input(f"Введите значение {list_xyz[i]}: "))

left = not (list[0] or list[1] or list[2])
right = not list[0] and not list[1] and not list[2]

if (left == right) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")