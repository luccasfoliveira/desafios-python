from random import randint

aleatorias = [randint(1, 50) for i in range(10)]
print(*aleatorias)

for i in range(len(aleatorias)):
    menor = i
    for j in range(i+1, len(aleatorias)):
        if aleatorias[j] < aleatorias[menor]:
            menor = j
    aleatorias[menor], aleatorias[i] = aleatorias[i], aleatorias[menor]
print(*aleatorias)
