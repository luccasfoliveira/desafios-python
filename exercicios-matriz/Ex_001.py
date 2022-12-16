"""
1.) Elabore um programa que leia uma matriz 5x5 e calcule e mostre a diagonal principal.
"""
from random import randint

print('Digite a dimenssão da Matriz')
linha = int(input('>>> '))
print()
A = [0]*linha
for i in range(linha):
    A[i] = [0]*linha
    for j in range(linha):
        A[i][j] = randint(10, 50)
    print(*A[i])
print()
for i in range(len(A)):
    print(A[i][i], end=' ')
