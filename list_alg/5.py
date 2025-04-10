import random
n = 3
a = [random.randint(-10, 10) for i in range(n)]
print(a)

# максимальный элемент списка
ans = -10**12
for i in range(n):
    if a[i] > ans:
        ans = a[i]
print(ans)