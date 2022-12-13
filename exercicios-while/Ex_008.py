soma = 0
while True:
    preco = float(input('Preço>>> '))
    if preco == 0:
        break
    qnt = int(input('Qnt>>> '))
    soma += preco * qnt
print('Total:', f'R${soma:.2f}')
