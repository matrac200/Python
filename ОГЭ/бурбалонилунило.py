x = int(input())
s = 0
while x != 0:
    if x % 4 == 0 or x % 9 == 0:
        s += x
    x = int(input())
print (s)
