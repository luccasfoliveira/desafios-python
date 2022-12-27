from random import randint

numeros = [randint(0, 100) for i in range(20)]
print(numeros)

pares = [i for i in numeros if i % 2 == 0]
impares = [i for i in numeros if i % 2 != 0]

print(f'\nNúmeros Pares:', *pares, '\n'
      f'Números Ímpares:', *impares)
