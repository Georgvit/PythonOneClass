# Вычислить число c заданной точностью d
#
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

# Выводим число Пи
pi = math.pi
print(f'Pi = {pi}')

start = 1
end = 10 ** (-10)
count = 0
while start > end:
    count += 1
    start = start / 10
    print(f'Заданная точность {start}')
    print(f'Число Пи с заданной точностью {round(pi, count)}')


