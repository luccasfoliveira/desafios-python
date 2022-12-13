while True:
    a, b = input('>>> ').split()
    a, b = int(a), int(b)
    operador = input('[+] SOMA\n'
                 '[-] SUBTRAÇÃO\n'
                 '[*] MULTIPLICAÇÃO\n'
                 '[/] DIVISÃO\n'
                 '[#] SAIR DO PROGRAMA\n'
                 '>>> ')

    if operador == '#':
        break
    soma = a+b
    if operador == '-':
        soma = a-b
    elif operador == '*':
        soma = a*b
    elif operador == '/':
        if b == 0:
            print('divisor é igual 0')
            continue
        else:
            soma = a/b
    print(a, operador, b, '=', soma)
