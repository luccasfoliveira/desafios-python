from random import randint

gabarito = [chr(randint(ord('a'), ord('e'))) for i in range(10)]

while True:
    respostas = [chr(randint(ord('a'), ord('e'))) for i in range(10)]
    print(f'{gabarito}\n'
          f'{respostas}')

    cont = 0
    for i in range(10):
        if gabarito[i] == respostas[i]: cont += 1

    print(f'Nota: {cont}')
    print('Aluno aprovado' if cont > 6 else 'Aluno reprovado')

    while True:
        resp = input('\nExiste outro candidato [S/N]? ').upper().split()[0]
        if resp not in ['S', 'N']: print('Resposta Inválida...')
        else: break
    if resp == 'N': break
