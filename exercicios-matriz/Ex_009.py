A = [0]*8
for i in range(8):
    A[i] = [0]*8
    for j in range(8):
        A[i][j] = (i+j) % 2
    print(*A[i])
