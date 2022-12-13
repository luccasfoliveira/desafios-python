# Resumos e Conceitos 📚📚📚

<h3 align="center"> 
    🚨  Vale destacar que os textos são de minha autoria, e baseados nos meus estudos, desconsidere (se houver) erros gramaticais, e não leve este conteúdo a rigor  🚨
</h3>

# Índice

* [Página Principal](README.md)

* [Entrada e Saída](#Entrada-e-Saída)
* [Sequenciais](#Sequenciais)
* [Estrutura de Controle - Condições](#Estrutura-de-Controle---Condições)
* [Estrutura de Repetições](#Estrutura-de-Repetições)
* [Listas](#Listas)
* [Matrizes](#Matrizes)
* [Dicionários](#dicionários)
* [Tuplas](#Tuplas)
* [Funções](#Funcoes)

# Dicionários

Dicionário - type(dict) - {   } - chave - valor


Conceito

O Dicionário é uma estrutura de dados parecida com a Lista,
nele você armazena elementos compostos por chaves e valores
("uma ordem de duas informações"), ou seja, cada elemento é
agrupado por uma chave (na qual seria o índice) e um valor
(o valor seria o conteúdo). O acesso a estes elementos são
por suas respectivas chaves, onde cada chave pode ser
qualquer tipo de valor (int, float, str, tupla, lista...),
diferente das listas, onde sua forma de acesso aos elementos
são por índices de valor inteiro (lista[int]), deste modo,
para acessarmos um elemento (valor ou conteúdo) de um dicionário,
basta você acessar atravéz da sua chave (dicionario[chave]),
onde o resultado será o valor.
____________________________________________________________
Há algumas maneiras de você criar um dicionário, tanto vazio
quanto com alguns elementos, ou então ir adicionando:

~~~python
 # dicionario vazio
 dicionario = {} 

 # dicionario criado já com seus respetivos elementos
 dicionario = {"Nome": "Luccas", "Idade": 27, "Cursando": True}

 # adicionando elementos ao dicionario
 dicionario[<chave>] = valor
 '''neste caso se a chave não estiver no dicionário, o Python
 automaticamente adiciona esta chave e valor à estrutua, se
 não, ele atualiza o valor correspondente a chave.'''
~~~



Alguns Comandos:

Alguns comandos, métodos e funcionalidades para manipulação
desta estrutura:

Vimos como criar e adicionar um elemento (conjunto de chave e
valor) no dicionário, agora iremos realizar a remoção de
elementos do dict. A remoção pode ser feita em três formas
similares com os métodos:

<dicionario>.pop(chave);
<dicionario>.popitem();
e o comando del dicionario[chave]:

 .pop(chave) realiza a remoção de um elemento
 específico e o retorna com o valor desejado;

 .popitem() realiza a remoção do último elemento do
 dicionário, e também retorna o valor removido; e

 o comando del dicionario[chave] apenas remove o
 elemento desejado.

Sabendo adicionar e remover elementos de um dicionário, agora
vamos usar alguns métodos para acessar esses elementos. Os
métodos dicionario.items(); dicionario.keys(); e
dicionario.values() são métodos para termos acesso aos
respectivos valores:

~~~python
 <dicionario>.items() # Irá gerar uma lista contendo todos os elementos (dentro de uma tupla) do dicionário;

 <dicionario>.keys() # Irá gerar uma lista com todas as chaves do dicionário;

 <dicionario>.values() # Irá gerar uma lista com todas os valores do dicionário.
~~~
  
Para estes três métodos, você pode usar o <for> desta maneira:

~~~python
 # note que .items() gera chave e valor, portanto
 # pode usar duas variáveis auxiliares (chave, valor)
 for chave, valor in <dicionario>.items():
  print(chave, valor)

 for chave in <dicionario>.keys():
  print(chave)

 for valor in <dicionario>.values():
  print(chave)
~~~

Outra maneira de você acessar um dicionário é usando o método
<dicinario>.get(chave) - este métodos é muito útil quando
você quer saber se um elemento está contido no dicionário:

 Se usarmos <dicinario>.get(chave) e esta chave está no
 dicionário, ele irá retornar o valor, senão, retornará
 None (None = nenhum valor, nada);

 Senão se definirmos <dicinario>.get(chave, 0) ele irá
 retornar o valor se houver, senão, o valor do segundo
 parâmetro, se não for especificado o segundo parâmetro,
 retornará None.

Irei explicar no mais tardar, o que seria Tabela Hash (função hash),
que no conceito Dicionário é de suma importância.

_____________________________________________________________________

 # Tuplas
 
Tupla - type(tuple) - (   ) - imutável


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
 tupla = <valor>,

 # sem a vírgula o tipo seria inteiro (neste caso)
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
