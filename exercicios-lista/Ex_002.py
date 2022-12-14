from random import randint

lista1 = [0] * 10
lista2 = [0] * 10
lista3 = []

for i in range(10):
    lista1[i] = randint(0, 10)
    lista2[i] = randint(0, 10)
    lista3.append(lista1[i] + lista2[i])
print(lista1)
print(lista2)
print(lista3)
