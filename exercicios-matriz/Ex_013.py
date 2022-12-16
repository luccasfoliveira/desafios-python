from random import randint

A = [0]*5
for i in range(len(A)):
    A[i] = [0] * 5
    for j in range(len(A)):
        A[i][j] = int(input('>>> '))

sim = True
for i in range(len(A)):
    print(*A[i])
    for j in range(1, len(A)):
        if A[i][j] != A[j][i] and A[i][i] != 0:
            sim = False
            break

# testando operadores ternários
# há 3 métodos - 1º recom.; 2º não é boa prática; 3º estilo "antigo"
print('Identidade' if sim else 'Não é Identidade')
print(('Não é identidade', 'Identidade')[sim])
print(sim and 'Identidade' or 'Não Identidade')
