fibonacci = [1]
x = 1
soma = 0
for i in range(19):
    x = x + soma
    soma = x - soma
    fibonacci.append(x)
print(fibonacci)
