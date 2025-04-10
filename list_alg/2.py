import random
n = 10
a = [random.randint(-10, 10) for i in range(n)]
print(a)

# все четные элементы возвести в квадрат
for i in a:
    if i % 2 == 0:
        i = i ** 2
print(a) # так работать не будет

for i in range(n):
    if a[i] % 2 == 0:
        a[i] = a[i] ** 2
print(a) # а так будет