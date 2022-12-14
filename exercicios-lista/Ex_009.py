fibonacci = [1]
x , soma = 1, 0
for i in range(19):
    x = x + soma
    soma = x - soma
    fibonacci.append(x)
print(fibonacci)
