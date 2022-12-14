from random import randint

a = []
b = []
for i in range(10):
    a.append(randint(0, 10))
    b.append(randint(0, 10))
print(f'a = {a}\nb = {b}')

c = []
for i in a:
    if i not in c:
        c.append(i)
for i in b:
    if i not in c:
        c.append(i)
print(f'c = {c}')
