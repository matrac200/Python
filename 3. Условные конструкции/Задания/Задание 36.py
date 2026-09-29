a = int(input())
b = int(input())
c = int(input())
h = max(a, b, c)
k1 = min(a, b, c)
k2 = a + b + c - h - k1
if k1 + k2 <= h:
    print ('не существует')
elif k1**2 + k2**2 == h**2:
    print('прямоугольный')
elif k1**2 + k2**2 < h**2:
    print('тупоугольный')
elif k1**2 + k2**2 > h**2:
    print('остроугольный')