def potencia(base, expoente):
    """
    :param base: int
    :param expoente: int
    :return: potência ou exceção se
    expoente for menor que 0
    """
    if expoente < 0:
        return 'expoente tem que ser maior ou igual a 0.'
    return base ** expoente


print(potencia(2, 2))
print(potencia(3, 2))
print(potencia(4, 2))
print(potencia(5, 2))
print(potencia(2, -1))
