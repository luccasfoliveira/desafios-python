class GerarVetor:
    """
    classe: gerar um vetor
    """
    def __init__(self):
        self.vetor = list()

    def gerar_vetor(self, tamanho):

        """
        :param tamanho: int
        :return: gera vetor com tamanho n
        """

        from random import randint

        while len(self.vetor) != tamanho:
            e = randint(10, 50)
            if e not in self.vetor:
                self.vetor.append(e)

    def imprimir_vetor(self):
        """
        :return: o prórpio vetor
        """

        return self.vetor

    def ordenar_vetor(self):
        """
        :return: vetor ordenado com a função sorted
        """

        self.vetor = sorted(self.vetor)
        return self.vetor

    def buscar_elemento(self, elemento):
        """
        :param elemento: int
        :return: posição do valor se houver
        ou -1 caso não exista (bisca binária)
        """

        vetor = self.ordenar_vetor()

        # cariáveis para manipular a busca
        inicio = 0
        fim = len(vetor)//2 - 1

        while inicio <= fim:

            # meio = indice
            meio = (inicio + fim) // 2

            # chute = elemento
            chute = vetor[meio]
            if chute == elemento:
                return meio
            elif chute > elemento:
                fim = meio - 1
            else:
                inicio = meio + 1
        return -1

    def maior_elemento(self):
        """
        :return: maior elemento
        """

        maior = self.vetor[0]
        for i in self.vetor[1::]:
            if maior < i:
                maior = i
        return maior

    def menor_elemento(self):
        """
        :return: menor elemento
        """
        menor = self.vetor[0]
        for i in self.vetor[1::]:
            if menor > i:
                menor = i
        return menor

    def media_valor(self):
        """
        :return: media entre os elementos
        """
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
