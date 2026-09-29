n = int(input())
s = 0
for i in range(n):
    x = int(input())
    if x % 7 == 1:
        s += x
print(s)