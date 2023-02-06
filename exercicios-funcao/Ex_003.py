def crescente(a, b, c):
    """
    :param a: int
    :param b: int
    :param c: int
    :return: ordem crescente
    """
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a, b, c


print(*crescente(3, 2, 1))
print(*crescente(8, 9, 7))
print(*crescente(11, 6, 9))
print(*crescente(4, 10, 6))
