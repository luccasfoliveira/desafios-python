# Resumos e Conceitos
# Índice 



* [Dicionários](#dicionários)
* [Entrada e Saída](#Entrada-e-Saída)
* [Sequenciais](#Sequenciais)
* [Estrutura de Controle - Condições](#Estrutura-de-Controle---Condições)
* [Estrutura de Repetições](#Estrutura-de-Repetições)
* [Listas](#Listas)
* [Matrizes](#Matrizes)
* [Tuplas](#Tuplas)
* [Funções](#Funcoes)

## [Dicionários](#dicionários)

Dicionário - type(dict) - {} - chave - valor
___________
#### **Conceito:**

O Dicionário é uma estrutura de dados parecida com a Lista,
nele você armazena elementos compostos por chaves e valores
("uma ordem de duas informações"), ou seja, cada elemento é 
agrupado por uma chave (na qual seria o índice) e um valor 
(o valor seria o conteúdo). O acesso a estes elementos são
por suas respectivas chaves, onde cada chave pode ser
qualquer tipo de valor (int, float, str, tupla, lista...), 
diferente das listas, onde sua forma de acesso aos elementos 
são por índices de valor inteiro (lista[<int>]), deste modo,
para acessarmos um elemento (valor ou conteúdo) de um dicionário,
basta você acessar atravéz da sua chave (dicionario[<chave>]),
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
dicionario[<chave>] = <valor>
'''neste caso se a chave não estiver no dicionário, o Python
automaticamente adiciona esta chave e valor à estrutua, se
não, ele atualiza o valor correspondente a chave.'''
~~~
__________________
#### **Alguns Comandos:**

Alguns comandos, métodos e funcionalidades para manipulação 
desta estrutura:

Vimos como criar e adicionar um elemento (conjunto de chave e 
valor) no dicionário, agora iremos realizar a remoção de 
elementos do dict. A remoção pode ser feita em três formas 
similares com os métodos:


<dicionario>.pop(<chave>); 
<dicionario>.popitem(); 
e o comando del <dicionario[<chave>]>:

	.pop(<chave>) realiza a remoção de um elemento 
	específico e o retorna com o valor desejado;

	.popitem() realiza a remoção do último elemento do 
	dicionário, e também retorna o valor removido; e

	o comando del <dicionario[<chave>]> apenas remove o 
	elemento desejado.

Sabendo adicionar e remover elementos de um dicionário, agora 
vamos usar alguns métodos para acessar esses elementos. Os 
métodos <dicionario>.items(); <dicionario>.keys(); e 
<dicionario>.values() são métodos para termos acesso aos 
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
<dicinario>.get(<chave>) - este métodos é muito útil quando
você quer saber se um elemento está contido no dicionário:

	Se usarmos <dicinario>.get(<chave>) e esta chave está no
	dicionário, ele irá retornar o valor, senão, retornará
	None (None = nenhum valor, nada);

	Senão se definirmos <dicinario>.get(<chave>, 0) ele irá 
	retornar o valor se houver, senão, o valor do segundo 
	parâmetro, se não for especificado o segundo parâmetro,
	retornará None.

Irei explicar no mais tardar, o que seria Tabela Hash (função hash),
que no conceito Dicionário é de suma importância.
