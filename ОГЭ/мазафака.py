x = int(input())
s = 0
while x != 0:
    if x % 4 == 0 and x % 10 == 8:
        s += x
    x = int(input())
print(s)