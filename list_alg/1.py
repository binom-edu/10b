import random
n = 3
a = [random.randint(-10, 10) for i in range(n)]
print(a)

for i in range(n):
    print(a[i]) # i - индекс элемента

print('---')

for i in a:
    print(i) # i - сам элемент