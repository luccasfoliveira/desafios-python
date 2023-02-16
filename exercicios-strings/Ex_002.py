texto = input("Texto: ")
verificadas = list()
for vogal in texto:
    if vogal in ['A', 'E', 'I', 'O', 'U'] and vogal not in verificadas:
        print(f'{vogal} = {texto.count(vogal)}')
        verificadas.append(vogal)
    elif vogal in ['a', 'e', 'i', 'o', 'u'] and vogal not in verificadas:
        print(f'{vogal} = {texto.count(vogal)}')
        verificadas.append(vogal)
