from random import randint

A = [0]*3
for i in range(len(A)):
    A[i] = [0] * 3
    for j in range(len(A)):
        A[i][j] = int(input('>>> '))
    print(*A[i])

sim = True
for i in range(len(A)):
    for j in range(1, len(A)):
        if A[i][j] != A[j][i] and A[i][i] != 0:
            sim = False
            break

print('Identidade' if sim else 'Não é Identidade')
print(('Não é identidade', 'Identidade')[sim])
print(sim and 'Identidade' or 'Não Identidade')
