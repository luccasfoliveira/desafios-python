def maior(num1, num2):
    """
    :param num1: int
    :param num2: int
    :return: o maior entre eles
    """
    maior = num1
    if num2 > num1:
        maior = num2
    return maior


print(maior(2, 3))
print(maior(8, 16))
print(maior(17, 3))
print(maior(5, 5))
