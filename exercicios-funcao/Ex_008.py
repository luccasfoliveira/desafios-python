def primo(num):
    """
    :param num: int
    :return: True para primo False não primo
    """
    if (num % 2 == 0 and num != 2) or num <= 1:
        return False
    else:
        for i in range(3, int(num**.5)+1):
            if num % i == 0:
                return False
        return True


print(primo(1))
print(primo(2))
print(primo(3))
print(primo(9))
print(primo(6))
print(primo(7))
print(primo(8))
