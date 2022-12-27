from random import randint

while True:
    lista = [randint(0, 10) for i in range(10)]

    while True:
        n = int(input('\nDigite um valor positivo de 1 a 10: '))
        if n < 0 or n > 10: print('Digite novamente...')
        else: break

    cont = 0
    for i in lista:
        if n == i: cont += 1
    if cont == 0: print('Não consta na lista...')
    else: print(f'Aparece {cont}x\n'
              f'{lista}')

    resp = input('Deseja continuar [S/N]? ').upper().split()[0]
    if resp == 'N': break
