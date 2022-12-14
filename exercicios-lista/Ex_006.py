from random import randint

numeros = []
for i in range(20):
    numeros.append(randint(0, 100))
print(*numeros)

pares = []
impares = []
for i in numeros:
    pares.append(i) if i % 2 == 0 else impares.append(i)

print(f'\nNúmeros Pares: {pares}\n'
      f'Números Ímpares: {impares}')
