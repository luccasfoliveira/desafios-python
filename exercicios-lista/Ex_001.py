lista = [int(input(f'Digite o {i + 1}º valor: ')) for i in range(10)]

maior = menor = lista[0]

for i in range(1, 10):
    if lista[i] > maior: maior = lista[i]
    elif lista[i] < menor: menor = lista[i]

print(f'Maior: {maior}\n'
      f'Menor: {menor}')
