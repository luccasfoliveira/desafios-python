"""
7.) Elabore um programa que leia uma matriz 4x6 e
calcule e mostre a sua matriz transposta equivalente.
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
T = [0]*len(A[0])
for i in range(len(T)):
    T[i] = [0]*len(A)
    for j in range(len(T[0])):
        T[i][j] = A[j][i]
    print(*T[i])
