# Listas

Lista - type(list) - [  ] - mutável
_________
Conceito:

Lista é uma estrutura de dados capaz de amarzenar mais de um tipo valor, ou seja,
você cria uma variável composta por diversos valores (vetor), ou se preferir uma
lista/vetor vazio. As listas tem a função de guardar vários valores, e o acesso
a esses valores é definido por meios de seus índices que são valores int.

_________________________________________________________________________________
Há algumas maneiras de você criar uma lista, vazia ou com alguns elementos, as
categorias de valores que podem ser inseridos numa lista inclui qualquer um:
int., str., bool, tupla, dict., ou até mesmo uma lista dentro de uma lista,
vejamos alguns exemplos:
~~~python
            # lista vazia
            lista = []
            lista = list()

            # lista já com valores definidos
            lista = [1, 2, 3, 4, 5, 6, 7]
            lista = ['Luccas', 'Lindo', True, 27.0]

            # ou se preferir, você pode já estabelecer um espaço na memória
            lista = [0]*10 # lista tamanho 10, todos valores = 0
~~~

__________________
Alguns comandos, métodos e funcionalidades para manipulação
desta estrutura:

Vimos como criar lista, e sabemos que o acesso aos elementos da lista ocorre por índices,
por exemplo:
~~~python
            lista = [1, 2, 3, 4, 5, 6, 7]
            lista[0] # --> 1
            lista[1] # --> 2
~~~
Podemos também acessar os valores com valores negativos, veja:
~~~python
            lista = [1, 2, 3, 4, 5, 6, 7]
            lista[-1] # --> 7
            lista[-2] # --> 6
~~~

Como em Python os índices começam com o valor 0, sabemos que uma lista com tamanho sete,
o índice vai até seis (0=1, 1=2, 2=3, 3=4, 4=5, 5=6, 6=7, no caso do exemplo acima),
e para descobrirmos o tamnho da lista, usamos a função len(), esta
função retorna um número inteiro, demosntrando a quantidade de elementos contidos numa
lista, aqui não podemos confundir o número que a função len() retorna com os índices,
isto pode acorrer quando usamos a funcionalidade for, para percorrer uma lista.

Uma maneira de adicionarmos um item numa lista é usando o método .apeend(), com ele você
consegue adicionar o valor que deseja na última posição da lista, há uma outra maneira de
"adicionar" (trocar) um elemento da lista, quando você já tem os elementos definidos, usando
a sintaxe lista[indice] = valor:
~~~python
            lista = [1, 2, 3, 4, 5, 6, 7]
            lista.append(8) # lista = [1, 2, 3, 4, 5, 6, 7, 8]

            lista[3] = -4
            lista = [1, 2, 3, -4, 5, 6, 7]
~~~
O métodos .extend([]) também adiciona uma lista dentro de outra lista, também podemos pensar que ele
faz um update da lista que vocçe seja expandir, ele trabalha o objeto de forma iteravel, percorrendo-a, vejamos:
~~~python
            lista = [1, 2, 3, 4, 5, 6, 7]
            lista.extend([1, 2, 3, 4]) # lista = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4]

            lista.append([1, 2, 3])
            lista = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, [1, 2, 3]]
~~~
Note que o .append() trabalha de forma grosseira, e simplesmente adiciona o objeto por completo, já na .extend(),
ele analisa o objeto, faz a iteração dos elementos de forma única, e os transoformas em elementos.

Outro método importante no mundo da lista é o .pop(), e o del lista[indice]. Estes dois
comandos removem o elemento da lista, e o método .clear(), apaga toda a lista. Vale ressaltar que
o método .pop(), se não definido o indíce para ser removido, ele sempre removerá o último por
padrão, e ainda, nos retornará o valor removido, e o comando del não retorna nenhum valor e simplesmente
apagará o valor que foi especidicado no índice, vejamos:
~~~python
            lista = [1, 2, 3, 4, 5, 6, 7]
            x = lista.pop(3) #
            x = 4
            lista = [1, 2, 3, 5, 6, 7]
            lista.pop()
            7
            del a[0]
            lista = [2, 3, 5, 6, 7]
~~~


# Lista de Exercícios com Listas:

1.) [Faça um algoritmo que leia um vetor de 10 números inteiros e calcule e mostre o maior  e o menor elementos do vetor.](Ex_001.py)

2.) [Elabore um algoritmo que leia 2 vetores de 10 números inteiros cada e em seguida calcule e imprima um terceiro vetor formado pela soma dos valores respectivos dos vetores lidos.](Ex_002.py)

3.) [Elabore um algoritmo que crie um vetor capaz de armazenar os 20 primeiros valores ímpares.](Ex_003.py)

4.) [Elabore um algoritmo que leia dois vetores de 10 valores cada e calcule o produto escalar entre eles:
	PE =  A[0]*B[0] + A[1]*B[1] + A[2]*B[2] + A[3]*B[3] + ... + A[9]*B[9]](Ex_004.py)
  
5.) [Elabore um programa que leia um vetor capaz de armazenar 10 números e em seguida, leia um valor e verifique se este valor existe ou não no vetor lido. Caso ele exista, indique quantas vezes ele aparece no vetor.](Ex_005.py)

6.) [Elabore um algoritmo que leia um vetor capaz de armazenar 20 valores inteiros e, em seguida, gere outros dois vetores, um formado  pelos valores pares e o outro pelos valores ímpares.](Ex_006.py)

7.) [Elabore um algoritmo que leia um vetor com 20 elementos. A seguir, troque o primeiro elemento com o décimo primeiro, o segundo com o décimo segundo, etc., e mostre o vetor assim modificado.](Ex_007.py)

8.) [Elabore um algoritmo que leia um vetor de 10 caracteres (a, b, c, d ou e) que é o gabarito de uma prova de múltipla escolha aplicada a vários candidatos. Em seguida leia o vetor resposta de cada candidato (também um vetor de 10 caracteres) e mostre a nota resultante do candidato (0 a 10).  Repita o processo enquanto existir candidato para ser avaliado.](Ex_008.py)

9.) [Elabore um algoritmo que gere um vetor contendo os 20 primeiros valores da série de Fibonacci.](Ex_009.py)

10.) [Elabore um algoritmo que leia dois (A e B) vetores de 10 elementos inteiros cada. Calcule um terceiro vetor formado pela intersecção ( C ) dos vetores lidos. (Elementos que existem em ambos os vetores A e B, não importando suas posições).](Ex_010.py)

11.) [Idem ao 10, porem gerando o vetor união de A com B (Todos os elementos de A e somente os elementos de B que não existem em A).](Ex_011.py)

12.) [Elabore um algoritmo que leia um vetor de 10 elementos e ordene os vetores de forma crescente. (Pesquise o algoritmo Bubble Sort).](Ex_012.py)

13.) [Idem ao 12) para o algoritmo  Select Sort.](Ex_013.py)

14.) [Elabore um algoritmo que leia dois vetores A e B de 10 elementos cada (já ordenados de forma crescente) e calcule o vetor C, formado pela intercalação dos vetores lidos (A e B).](Ex_014.py)
