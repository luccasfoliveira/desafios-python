"""
3.) Elabore um programa que leia uma matriz 5x5 e mostre os elementos do triângulo superior direito da matriz
(elementos acima da diagonal principal).
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
    for j in range(i+1, len(A)):
        print(A[i][j], end=' ')
