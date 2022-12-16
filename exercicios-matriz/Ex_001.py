"""
1.) Elabore um programa que leia uma matriz 5x5 e calcule e mostre a diagonal principal.
"""
from random import randint

print('Digite os elementos da Matriz')
linha = int(input('Quantas Linhas tem a Matriz>>> '))
coluna = int(input('Quantas Colunas tem a Matriz>>> '))
print()
A = [0]*linha
for i in range(linha):
    A[i] = [0]*coluna
    for j in range(coluna):
        A[i][j] = randint(10, 50)
    print(*A[i])
print()
if linha == coluna:
    for i in range(len(A)):
        print(A[i][i])
else:
    print('Não é Matriz Quadrada')
