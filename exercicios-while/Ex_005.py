n = int(input('>>> '))
while n > 0:
    inv = inv * 10 + (n % 10)
    n //= 10
print(inv)
