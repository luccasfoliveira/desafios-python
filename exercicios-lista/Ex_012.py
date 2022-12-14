from random import randint

a = []
for i in range(10):
    a.append(randint(0, 50))
print(*a)
for i in range(10):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(*a)
