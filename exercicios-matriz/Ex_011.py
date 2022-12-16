linha = int(input('Quantas Linhas tem a Matriz>>> '))
coluna = int(input('Quantas Colunas tem a Matriz>>> '))
print()
A = [0]*linha
for i in range(len(A)):
    A[i] = [0]*coluna
    for j in range(len(A)):
        if i == j or i + j == len(A)-1:
            A[i][j] = 1
    print(*A[i])

