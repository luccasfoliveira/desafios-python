a, b = [], []

while True:
    num = int(input('Digite o número do conjunto a: '))
    if num in a: print('Número repetido, digite novamente...\n')
    else:
        a.append(num)
        if len(a) == 5:
            print()
            break
while True:
    num = int(input('Digite um número do conjunto b: '))
    if num in b: print('Número repetido, digite novamente...\n')
    else:
        b.append(num)
        if len(b) == 5: break

print(f'a = {a}\nb = {b}')

c = [i for i in a if i in b and i not in c]
print(f'\nc = {c}')
