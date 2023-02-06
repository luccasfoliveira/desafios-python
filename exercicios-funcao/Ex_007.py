def inverte(num):
    """
    :param num: int
    :return: número invertido
    """
    num = str(num)
    return int(num[::-1])


print(inverte(123))
print(inverte(432))
print(inverte(896))
