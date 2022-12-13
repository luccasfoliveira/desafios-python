x = 0
soma = apr = rep = 0
while x <= 59:
    n1 = float(input('>>> '))
    n2 = float(input('>>> '))
    media = (n1 + n2) / 2
    if media >= 6:
        print('APROVADO:', f'{media:.2f}')
        apr += 1
    else:
        print('REPROVADO', f'{media:.2f}')
        rep += 1
    soma += media
    x += 1
print('MÉDIA GERAL:', f'{soma / x:.2f}')
print('APROVADOS:', apr)
print('REPROVADOS:', rep)
