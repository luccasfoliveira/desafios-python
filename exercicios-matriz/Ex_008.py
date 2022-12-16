"""
8.) Elabore um programa que leia uma matriz 5x5 e  verifique se esta matriz é simétrica.
Uma matriz para ser simétrica deve ter A[i][j] == A[j][i] para todo i e j válidos. Veja o exemplo abaixo de simetria
"""
linhas = int(input('Linhas>>> '))
colunas = int(input('Colunas>>> '))
print()
A = [0]*linhas
for i in range(linhas):
    A[i] = [0]*colunas
    for j in range(colunas):
        A[i][j] = int(input('>>> '))
print(*A)

sim = True
for i in range(linhas):
    for j in range(1, colunas):
        if A[i][j] != A[j][i]:
            sim = False
            break
print('É simétrica' if sim else 'Não é simétrica')
