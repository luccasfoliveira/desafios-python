from random import randint

a = [randint(0, 50) for i in range(10)]

for i in range(10):
    for j in range(i, len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(*a)
