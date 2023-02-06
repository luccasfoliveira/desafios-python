def divisao(dividendo, divisor):
    """
    :param dividendo: float
    :param divisor:
    :return: divisão ou exceção
    """
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return 'divisão não pode ser zero'
    except:
        return 'digite um número'


print(divisao(5, 9))
print(divisao(8, 3))
print(divisao(1.8, 9))
print(divisao(10, 1))
print(divisao(5, 0))
print(divisao(5, '9'))
