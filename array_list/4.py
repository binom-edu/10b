n = 10
a = []
for i in range(n):
    a.append(i)
print(a)
b = [i for i in range(n)]
print(b)
c = [i ** 2 for i in range(n)]
print(c)
d = [i for i in c if i % 10 == 6]
print(d)