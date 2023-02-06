from Ex_008 import primo

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
print(f'Primos entre {inicio} á {fim}:')
for i in range(inicio, fim+1):
    if primo(i):
        print(i)

