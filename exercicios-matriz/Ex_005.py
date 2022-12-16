"""
5.) Elabore um programa que leia uma matriz 5x5 e mostre os elementos do triângulo superior esquerdo da matriz
(elementos acima da diagonal secundária).
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
for i in range(len(A)-1):
    for j in range(len(A)-1-i):
        print(A[i][j])
