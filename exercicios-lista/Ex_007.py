from random import randint

lista = [randint(0, 100) for i in range(20)]
print(lista)
for i in range(10):
    aux = lista[i]
    lista[i] = lista[i + 10]
    lista[i + 10] = aux
print(lista)
'''
outra forma de realizar a troca de valores - desempacotamento 
lista[i], lista[i + 10] = lista[i + 10], lista[i]
'''
