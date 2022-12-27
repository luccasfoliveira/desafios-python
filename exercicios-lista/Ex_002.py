from random import randint

lista1 = [randint(0, 10) for i in range(10)]
lista2 = [randint(0, 10) for i in range(10)]
lista3 = [lista2[i] + lista1[i] for i in range(10)]

print(lista1)
print(lista2)
print(lista3)
