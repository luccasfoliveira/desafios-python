from random import randint

gabarito = []
for i in range(10):
    gabarito.append(chr(randint(ord('a'), ord('e'))))

while True:
    respostas = []
    for i in range(10):
        respostas.append(chr(randint(ord('a'), ord('e'))))
    print(f'{gabarito}\n'
          f'{respostas}')

    cont = 0
    for i in range(10):
        if gabarito[i] == respostas[i]:
            cont += 1

    print(f'Nota: {cont}')
    if cont > 6:
        print('Aluno aprovado\n')
    else:
        print('Aluno reprovado')

    while True:
        resp = input('\nExiste outro candidato [S/N]? ').upper().split()[0]
        if resp not in ['S', 'N']:
            print('Resposta Inválida...')
        else:
            break
    if resp == 'N':
        break
