"""
8.) Elabore um programa que leia uma matriz 5x5 e  verifique se esta matriz é simétrica.
Uma matriz para ser simétrica deve ter A[i][j] == A[j][i] para todo i e j válidos. Veja o exemplo abaixo de simetria
"""
print('Digite a dimenssão da Matriz')
linha = int(input('>>> '))
print()
A = [0]*linha
for i in range(linha):
    A[i] = [0]*linha
    for j in range(linha):
        A[i][j] = int(input('>>> '))

sim = True
for i in range(linha):
    print(*A[i])
    for j in range(1, linha):
        if A[i][j] != A[j][i]:
            sim = False
            break
print()
print('É simétrica' if sim else 'Não é simétrica')
