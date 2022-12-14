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
    print('Aluno aprovado\n' if cont > 6 else 'Aluno reprovado')

    while True:
        resp = input('\nExiste outro candidato [S/N]? ').upper().split()[0]
        if resp in ['S', 'N']: break
        print('Resposta Inválida...')

    if resp == 'N': break
