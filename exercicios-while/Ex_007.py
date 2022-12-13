soma = count = 0
while True:
    while True:
        idade = int(input('>>> '))
        if idade >= 0:
            count += 1
            break
        print('idade inválida')
    soma += idade
    if idade == 0:
        count -= 1
        break
print('Média das Idades:', f'{soma/count:.2f}')
