import random
n = 3
a = [random.randint(-10, 10) for i in range(n)]
print(a)

# сумма элементов массива
ans = 0
for i in range(n):
    ans += a[i]

print(ans)
print(sum(a))