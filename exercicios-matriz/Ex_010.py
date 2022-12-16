A = [0]*5
for i in range(len(A)):
    A[i] = [0] * 5
    for j in range(len(A)):
        A[i][j] = j * i
    print(*A[i])
