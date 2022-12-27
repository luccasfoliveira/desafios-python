from random import randint

a = [randint(0, 10) for i in range(10)]
b = [randint(0, 10) for i in range(10)]
print(f'a = {a}\nb = {b}')

c = []
for i in a:
    if i not in c:
        c.append(i)
for i in b:
    if i not in c:
        c.append(i)
print(f'c = {c}')
