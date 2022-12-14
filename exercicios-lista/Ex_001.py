lista = [0] * 10
for i in range(10):
    lista[i] = int(input(f'Digite o {i + 1}º valor: '))

maior = lista[0]
menor = lista[0]

for i in range(1, 10):
    if lista[i] > maior:
        maior = lista[i]
    elif lista[i] < menor:
        menor = lista[i]

print(f'Maior: {maior}\n'
      f'Menor: {menor}')
