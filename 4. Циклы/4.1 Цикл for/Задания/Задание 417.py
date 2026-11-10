n = int(input())
z = 0
m = 0
p = 0
d = 0
for i in range(n):
    x = int(input())
    if x == 0:
        z += 1
    if x < 0:
        m += 1
    if x > 0:
        p += x
        d += 1
print(f'Нулей: {z}')
print(f'Отрицательных: {m}')
print(f'Среднее положительных: {p/d:.2f}')



