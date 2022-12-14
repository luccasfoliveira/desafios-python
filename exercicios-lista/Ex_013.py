from random import randint

aleatorias = []
for i in range(10):
    aleatorias.append(randint(1, 50))
print(*aleatorias)

for i in range(len(aleatorias)):
    menor = i
    for j in range(i+1, len(aleatorias)):
        if aleatorias[j] < aleatorias[menor]:
            menor = j
    aleatorias[menor], aleatorias[i] = aleatorias[i], aleatorias[menor]
print(*aleatorias)
