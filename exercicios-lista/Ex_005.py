from random import randint

while True:
    lista = []
    for i in range(10):
        lista.append(randint(0, 10))

    while True:
        n = int(input('\nDigite um valor positivo de 1 a 10: '))
        if n >= 0 and n <= 10: break
        print('Digite novamente...')

    cont = 0
    for i in lista:
        if n == i:
            cont += 1
    print('Não consta na lista...' if cont == 0 else f'Aparece {cont}x\n{lista}')

    resp = input('Deseja continuar [S/N]? ').upper().split()[0]
    if resp == 'N': break
