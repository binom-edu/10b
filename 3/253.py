n = int(input())

x4 = n % 4 == 0
x100 = n % 100 == 0
x400 = n % 400 == 0

if x4 and not x100 or x400:
# if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('YES')
else:
    print('NO')