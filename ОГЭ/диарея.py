n = int(input())
s = 0
x = 0
for i in range (n):
    n = int(input())
    if n > 0:
        s += n
        x += 1
print(s / x)
print(x)