"""
12) Elabore um programa que leia uma matriz 4x12.
Cada coluna indica um mês do ano e cada linha uma semana do respectivo mês.
Os valores armazenados representam o total de peças produzidas por uma determinada fábrica.
Calcule:
a) Total de peças produzidas no ano;
b) Total de peças produzidas em cada mês;
c) Qual foi a semana e qual o mês onde houve a maior produção.
"""

from random import randint

A = [0]*4
meses = [0]*12
total = maior = semana = mes = 0
for i in range(4):
    A[i] = [0]*12
    for j in range(12):
        A[i][j] = randint(100, 1000)
        total += A[i][j]
        meses[j] += A[i][j]
        if A[i][j] > maior:
            maior = A[i][j]
            semana, mes = i+1, j+1
    print(str(i+1) + 'º semana:', *A[i])
print()
print(f'Total de peças produzidas: {total}')
for i in range(len(meses)):
    print(f'Total de peças do {i+1:02}º mês: {meses[i]}')
print(f'\nNa {semana}º semana e no {mes}º mês,\n'
      f'houve a maior produção: {maior} peças')
