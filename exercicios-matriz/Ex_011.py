print('Digite a dimenssão da Matriz')
linha = int(input('>>> '))
print()
A = [0]*linha
for i in range(len(A)):
    A[i] = [0]*linha
    for j in range(len(A)):
        if i == j or i + j == len(A)-1:
            A[i][j] = 1
    print(*A[i])

