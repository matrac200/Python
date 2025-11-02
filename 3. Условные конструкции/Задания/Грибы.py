x = int(input())
if x % 10 == 1 and x % 100 != 11:
    print('гриб')
elif 1 < x % 10 <= 4 and 15 < x % 100 < 11:
    print('гриба')
else:
    print('грибов')

