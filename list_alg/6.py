import random
n = 5
a = [random.randint(-10, 10) for i in range(n)]
print(a)

# количество пар соседних по индексу элементов с одинаковым знаком
ans = 0
for i in range(n - 1):
    x, y = a[i], a[i + 1]
    # if (x > 0 and y > 0) or (x < 0 and y < 0):
    if x * y > 0:
        ans += 1
print(ans)