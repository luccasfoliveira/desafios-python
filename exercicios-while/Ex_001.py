n = int(input('>>> '))
x, soma = 1, n
while n >= x:
    soma += n - x
    x += 1
print(soma)


def soma(num):
    # caso base
    if num == 1:
        return 1
    # caso recursivo
    return num + soma(num - 1)


print(soma(n))
