def maior(a, b):
    """
    :param a: int
    :param b: int
    :return: maior
    """
    maior = a
    if b > a:
        maior = b
    return maior


a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

# argumento recebido pelo usuário
print(maior(a, b))
