from random import randint

lista_1 = [0] * 10
lista_2 = [0] * 10
pe = 0
for i in range(10):
    lista_1[i] = randint(1, 10)
    lista_2[i] = randint(1, 10)
    pe = pe + lista_1[i] * lista_2[i]
    print(f'Multiplicando os valores do índice {i}\n'
          f'Lista 1: {lista_1[i]} x Lista 2: {lista_2[i]}\n'
          f'Produto Escalar do índice {i}: {pe}\n')