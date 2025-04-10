import random
n = 3
a = [random.randint(-10, 10) for i in range(n)]
print(a)

# среднее арифметическое четных элементов
cnt = 0
summ = 0
for i in range(n):
    if a[i] % 2 == 0:
        summ += a[i]
        cnt += 1

print(summ / cnt)