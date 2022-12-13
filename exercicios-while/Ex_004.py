n = int(input('>>> '))
x = 0
while 0 != n:
    n //= 10
    x += 1
print(x)
