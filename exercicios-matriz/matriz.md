# Matrizes

Quando eu falei que podemos inserir uma lista dentro de outra lista, torna-se uma lista bidimensional,
em ourtas palavras, podemos dizer matriz, vamos esclarecer a criação de matriz e como acessa-las:
~~~python
            from random import randint
            
            M = [0]*5
            for i in range(5):
                M[i] = [0]*5 # note que estou acessando o primeiro elemento e substituindo por uma lista
                for j in range(5):
                    # estou aqui acessando os elementos nas listas criadas anteriormente
                    # essa é a sintaxe o i correponde a linha e j a coluna
                    M[i][j] = randint(10, 50)
                print(*M[i])
                
            '''saida:
                    25 14 43 26 45
                    22 32 46 41 45
                    29 31 41 30 24
                    23 28 16 36 29
                    43 45 44 31 37'''
~~~
Notamos que para acessar um elemento de uma matriz precisamos de "dois índices", o primeiro índice seria
a linha que estamos e o segundo índice seria a coluna, neste caso se eu quero obter o número 36, eu utilizo
a sintaxe M[3][3] = 36 (na matriz gerada).


# Matrizes - Exercícios

1.) [Elabore um programa que leia uma matriz 5x5 e calcule e mostre a diagonal principal.](Ex_001)

![image](https://user-images.githubusercontent.com/102065560/208008758-4c2ee8e1-2c11-4df1-8a92-ba770cbd80f0.png)

2.) Elabore um programa que leia uma matriz 5x5 e calcule e mostre a diagonal secundária.

![image](https://user-images.githubusercontent.com/102065560/208007330-2aef0e3c-fc3f-4c48-947d-a6acf04d3291.png)/>

3.) Elabore um programa que leia uma matriz 5x5 e mostre os elementos do triângulo superior direito da matriz (elementos acima da diagonal principal).

![image](https://user-images.githubusercontent.com/102065560/208007371-b9844e5c-c0f7-4eee-b153-179c7b312fdc.png)

4.) Elabore um programa que leia uma matriz 5x5 e mostre os elementos do triângulo inferior esquerdo da matriz (elementos abaixo da diagonal principal).

![image](https://user-images.githubusercontent.com/102065560/208007386-ea34f2d0-f4a1-49a1-8760-e3d9a987d2a9.png)

5.) Elabore um programa que leia uma matriz 5x5 e mostre os elementos do triângulo superior esquerdo da matriz (elementos acima da diagonal secundária).

![image](https://user-images.githubusercontent.com/102065560/208007411-d49814bb-501f-4f79-923f-0304b63f97d8.png)

6.) Elabore um programa que leia uma matriz 5x5 e mostre os elementos do triângulo inferior direito da matriz (elementos abaixo da diagonal secundária).

![image](https://user-images.githubusercontent.com/102065560/208007419-6c02c34e-a57c-4dee-8922-016c93f04bb9.png)

7.) Elabore um programa que leia uma matriz 4x6 e calcule e mostre a sua matriz transposta equivalente.

![image](https://user-images.githubusercontent.com/102065560/208007436-b52a358c-9837-4bdc-bf37-453a80a97e90.png) ![image](https://user-images.githubusercontent.com/102065560/208007453-fcf330be-b325-4c3a-bc6d-5c7512a33d20.png)

8.) Elabore um programa que leia uma matriz 5x5 e  verifique se esta matriz é simétrica.  Uma matriz para ser simétrica deve ter A[i][j] == A[j][i] para todo i e j válidos. Veja o exemplo abaixo de simetria.

![image](https://user-images.githubusercontent.com/102065560/208007486-bb31f94f-8378-4409-b923-b411237b9e7b.png)

9.) Elabore um algoritmo que crie um tabuleiro de xadrez (8x8) colocando 0 nas casas brancas e 1 nas casas pretas.

![image](https://user-images.githubusercontent.com/102065560/208007802-f517acdd-d43b-4e5f-acef-5d831d2590f0.png)

10.) Elabore um algoritmo para gerar a seguinte matriz 5x5:

![image](https://user-images.githubusercontent.com/102065560/208007498-72bb6e76-fcf3-4e2c-8417-7d6333e1bb8a.png)

11.) Elabore um algoritmo para gerar a seguinte matriz 5x5:

![image](https://user-images.githubusercontent.com/102065560/208007513-7caff8a4-b6e0-47d4-b37a-bc5dc233d4a7.png)

12.) Elabore um programa que leia uma matriz 4x12. Cada coluna indica um mês do ano e cada linha uma semana do respectivo mês. Os valores armazenados representam o total de peças produzidas por uma determinada fábrica. Calcule:
a)	Total de peças produzidas em cada mês;
b)	Total de peças produzidas no ano;
c)	Qual foi a semana e qual o mês onde houve a maior produção.

![image](https://user-images.githubusercontent.com/102065560/208007538-437d6f5b-8859-4a34-8d7d-d639921f9743.png)

13.) Elabore um algoritmo que leia uma matriz 5x5 e verifique se ela é ou não uma matriz identidade.  Uma matriz é identidade se todos os elementos da diagonal principal são 1s e os demais 0s.

![image](https://user-images.githubusercontent.com/102065560/208007828-792a93c2-bbb3-457d-822a-1d304bf4fe7c.png)
