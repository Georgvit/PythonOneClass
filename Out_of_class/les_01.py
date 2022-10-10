num = []
num_two = ''

for i in range(1, 1000):
    if i % 2 != 0:
        num.append(i ** 3)
print(num)
for j in num:
    sum = 0
    for t in str(j):
        sum += int(t)
    if sum % 7 == 0:
        print(sum)

for j in range(len(num)):
    num[j] = num[j] + 17

print(num)

for j in num:
    sum = 0
    for t in str(j):
        sum += int(t)
    if sum % 7 == 0:
        print(sum)