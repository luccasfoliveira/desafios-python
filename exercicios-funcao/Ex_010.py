class GerarVetor:
    def __init__(self):
        self.vetor = list()

    def gerar_vetor(self, tamanho):
        from random import randint

        while len(self.vetor) != tamanho:
            e = randint(10, 50)
            if e not in self.vetor:
                self.vetor.append(e)

    def imprimir_vetor(self):
        return self.vetor

    def ordenar_vetor(self):
        self.vetor = sorted(self.vetor)
        return self.vetor

    def buscar_elemento(self, elemento):
        vetor = self.ordenar_vetor()

        inicio = 0
        fim = len(vetor)//2 - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            chute = vetor[meio]
            if chute == elemento:
                return meio
            elif chute > elemento:
                fim = meio - 1
            else:
                inicio = meio + 1
        return -1

    def maior_elemento(self):
        maior = self.vetor[0]
        for i in self.vetor[1::]:
            if maior < i:
                maior = i
        return maior

    def menor_elemento(self):
        menor = self.vetor[0]
        for i in self.vetor[1::]:
            if menor > i:
                menor = i
        return menor

    def media_valor(self):
        soma = self.vetor[0]
        for i in self.vetor[1::]:
            soma += i
        return soma / len(self.vetor)


lista = GerarVetor()
lista.gerar_vetor(10)
print(lista.imprimir_vetor())
print(lista.buscar_elemento(19))
lista.ordenar_vetor()
print(lista.imprimir_vetor())
print(lista.maior_elemento())
print(lista.menor_elemento())
print(lista.media_valor())
