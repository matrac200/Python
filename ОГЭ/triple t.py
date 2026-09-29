x = int(input())
s = 0
while x != 0:
    if x >= 100 and x < 1000 and x % 4 == 0:
        s += 1
    x = int(input())
print (s)