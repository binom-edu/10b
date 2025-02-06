n = int(input())

cnt = 0
while cnt < n:
    print('С Новым годом!', cnt)
    cnt += 1
    if cnt == 4:
        break
else:
    print('Блок else')
print('Конец программы')