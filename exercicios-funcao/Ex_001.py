def par_impar(num):
    """
    :param num: int
    :return: False para par; True para ímpar
    """
    try:
        if num % 2 == 0:
            return False
        else:
            return True
    except:
        return 'Digite um valor válido como parâmetro'


print(par_impar(5))
print(par_impar(6))
print(par_impar(10))
print(par_impar(7))
print(par_impar('5'))
