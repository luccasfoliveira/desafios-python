class GerarVetor:
    def __init__(self):
        self.vetor = list()

    def gerar_vetor(self, tamanho):
        from random import randint

        if len(self.vetor) != tamanho:
            e = randint(10, 50)
            if e not in self.vetor:
                self.vetor.append(e)

    def imprimir_vetor(self):
        return self.vetor

    def ordenar_vetor(self):
        return sorted(self.vetor)

    def buscar_elemento(self, elemento):
        vetor = self.ordenar_vetor()

        inicio = 0
        fim = len(vetor//2)-1

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


