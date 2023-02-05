
 # Tuplas
 
Tupla - type(tuple) - (  ) - imutável


Conceito

A tulpla é uma estrutura de dado que tem funcionalidades
também parecidas com as listas, porém, tuplas são imutáveis
com sua perspectiva de valores constantes, por serem imutáveis.
Há outra prorpriedade da tupla bastante útil na linguagem
Python, é o empacotamento e desempacotamento, onde você pode
ter o acesso aos valores da tupla de forma distributiva e
acessível, irei explcar melhor com exemplos.

O fato da tupla ser imutável, o elemento (qualquer tipo) que
compõe a tupla, não pode ser alterado, mas há (em Python) um
detalhe, se um dos elementos for uma estrutura de dados (lista
por exempplo), você consegue manipular apenas os elementos da
lista.
____________________________________________________________
Há algumas maneiras de você criar uma tupla, tanto vazia
quanto com alguns elementos, vejamos:

~~~python
 # tupla vazia
 tupla = ()

 # tupla com elementos
 tupla = (1, 2, 3, 4, 5)

 # empacotando tupla
 tupla = 100, 200, 300

 # note que neste caso há uma vírgula, a vírgula é necessária,
 # pois se não houvesse, a variável seria do tipo int., str,
 # float, o que for.
 tupla = <valor>  # sem a vírgula o tipo seria inteiro (neste caso)
 tupla = (1,)
~~~


Alguns Comandos

Os comandos feitos em tuplas são praticamentos iguais usados
em listas, excetos aqueles que alteram a estrutura, portanto,
você pode converter uma tupla em lista passando para uma
variável, concatenar (+), usar slice, e etc.

Há uma especialidade em tupla muito interessante, acredito
que só tenha na linguagem Python, que seria o empacotamento e
desempacotamento, vejamos alguns exemplos.

Criando esta estrutura, temos o tipo tupla, este tipo de
operação é chamado Empacotamento.

~~~python
    tupla = 100, 200, 300
~~~

O Desempacotamento seria você "destrinchar" os valores contidos
na tupla, separar os elementos, e referenciando-os nas variáveis
da seguinte forma:

~~~python
 a, b, c = tupla
 # Onde a variável a recebe o primeiro valor da tupla (100),
 # a variável b recebe o segundo valor da tupla (200), e assim
 # sucessivamente.
 # Ou:
 d, e = 10, 20
 # onde d recebe 10 e a variável e recebe 20
~~~

Essa especialidade do Python, é bastante útil quando você quer
realizar a operação de trocar valores entre variáveis sem usar
uma variável auxiliar (C = A, A = B, B = C == A, B = B, A). Isso
acontece, pois, em Python variável é um objeto, e ao ter um objeto,
o rótulo (nome da "variável"/ objeto) faz referência na memória
ao valor.

Há outro tipo de manuseio com o desempacotamento de tuplas, onde
se pode também ser realizado com listas, observemos os exemplos.

~~~python
 a = tuple(range(1, 11)
 # criei uma tupla contedo os valores de 1 a 10
~~~

Agora vamos desempacotar a tupla retornando uma lsita para uma
determinada variável, e um valor tipo inteiro para outra:

~~~python
 *b, c = a
 b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 c = 10
~~~

Note que o asterisco representa colocar todos os primeiros valores
na primeiro variável, e o que sobrar (no caso a última) o último
valor na última variável, Python não permite o desempacotamento de
uma tupla ou lista sem conter a quantidade de variáveis corresponte
ao tamanho da estrutura, contudo o asterisco ele manipula a estrutura
fazendo que agrupa todos os elementos menos o último como se fosse um
elemento, neste caso uma lista. Pasa tentar exemplificar s variáveis
correspondem aos índices da seguinte forma:

~~~python
 # sem asterisco:
 a = tuple(range(1, 11)
 b, c = a # erro de exceção
~~~

O caso acima apresentará erro, pois, o tamanho da tupla é maior que a
quantidade de variáveis para realizar a atribuição, neste caso, para
você conseguir repassar os valores às variáveis, o asterisco seria a
solução:

~~~python
 # sem asterisco:
 a = tuple(range(1, 11)

 b, *c = a
 //b = 1
 //c = [2, 3, 4, 5, 6, 7, 8, 9, 10]

 b, c, d = a # erro de exeção

 *b, c, d = a
 // b = [1, 2, 3, 4, 5, 6, 7, 8]
 // c = 9
 // d = 10

 b, *c, d = a
 // b = 1
 // c = [2, 3, 4, 5, 6, 7, 8, 9]
 // d = 10
~~~

Portanto, analisando o padrão, e entendo o último exemplo, podemos
entender que b, c, d se tornam índices da estrutura (claro com o
asterisco em uma das variáveis), e onde está o asterisco são repassados
os elementos em formato lista, e os demais valores int., mas pode ser
float, str, o que você estiver manipulando. Por exemplo, se na variável
a esteja guardada uma matriz de ordem três, e você queira repassar as
linhas nas respectivas variáveis (quantidade de variáveis == tamanho
da lista, se não houver asterisco), também é possível.

______________________________________________________________________________

# Exercícios com Tuplas:
