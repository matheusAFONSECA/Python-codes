# secao de estudos de estrutura de repetição, condição, controle de fluxo e de erros
"""A linguagem Python possui algumas estruturas para controle de execução de comandos. São elas: estruturas de
decisão e estruturas de repetição. Além disso, apresenta uma estrutura para lidar com erros e tratá-los"""

# ESTRUTURA DE CONDIÇÃO

"""As estruturas de decisão permitem impor condições ao código e distinguir quais ações
devem ser tomadas se forem verdadeiras ou falsas"""

# Utilizando a estrutura if...else
a = 2
if a < 5:
    print('A variavel a é menor que 5')
else:
    print('A variavel a é maior ou igual que 5')
# Resultado: A variavel a e menor que 5
"""A linguagem Python utiliza a indentação como uma forma de organização de
seus programas em blocos, por isso os comandos referente ao if ou else, precisam
estra dentro da indentação voltada a eles"""

# Utilizando apenas a estrutura if
a = 2
if a < 5:
    print('A variavel a e menor que 5')
# Resultado: A variavel a e menor que 5
"""a estrutura else não é necessária aqui porque a variável 'a' vai sempre satisfazer a condição da 
estrutura if, sendo ela desnecessária"""

# Utilizando a estrutura if...else, sem a incusao de comandos em else
a = 2
if a < 5:
    print('A variavel a e menor que 5')
else:
    pass
# Resultado: A variavel a e menor que 5
"""deve-se introduzir a palavrachave ‘pass’ na estrutura else para eliminar erros no programa, 
faz isso porque não queremos ter erros quanto a estrutura else"""

# Utilizando a estrutura if...else encadeada
a = 8
if a > 5:
    print('A variavel a é maior que 5')
    if a >= 5 & a < 7:
        print('A variavel a e maior ou igual a 5 e menor que 7')
        if a >= 7 & a <= 10:
            print('A variavel a e maior ou igual a 7 e menor que 10')
        else:
            print('A variavel a e maior que 10')

# Resultado: A variavel a é maior que 5
#            A variavel a e maior ou igual a 5 e menor que 7
#            A variavel a e maior ou igual a 7 e menor que 10

# Utilizando a estrutura if...else encadeada
a = 2
if a < 5:
    print('A variavel a e menor que 5')
# 'elif' se equipara a estrutura 'else if' em C++
elif a >= 5 & a < 7:
    print('A variavel a e maior ou igual a 5 e menor que 7')
elif a >= 7 & a < 10:
    print('A variavel a e maior ou igual a 7 e menor que 10')
else:
    print('A variavel a e maior que 10')
# Resultado: A variavel a e menor que 5

# Utilizando expressoes if...else
a = 6
print('A variavel a e menor que 5') if (a < 5) else print('A variavel a e maior ou igual que 5')
# Resultado: A variavel a e maior ou igual que 5

# ESTRUTURA DE REPETIÇÃO

# ESTRUTURA FOR
"""A estrutura for exerce um bloco de comandos por uma quantidade finita de vezes,
sendo limitada por um contador"""

# Utilizando a estrutura for
tupla = [1, 2, 3, 4, 5]
for x in tupla:
    print(x)
# Segue o mesmo principio da estrutura if, tem que seguir uma identação certa para funcionar
# Nesse exemplo foi usado para mostrar os elementos de uma tupla
# Resultado: 1
#            2
#            3
#            4
#            5

# Utilizando a estrutura for
for x in range(5):
    print(x)
# Aqui foi delimitado a quantidade de vezes (range) que um número iria ser mostrado
# Resultado: 1
#            2
#            3
#            4
#            5

# Utilizando a funcao range( ) com o laco for
for x in range(0, 10, 2):
    print(x)
# Nessa função range, o primeiro parâmetro mostra onde vai começar o contador, o segundo mostra até qual é
# o limite e o terceiro é o incremento
# Resultado: 0
#            2
#            4
#            6
#            8

# Utilizando a estrutura for... else
"""A estrutura for permite a integração de uma estrutura 
else, cujos comandos são executados após todos os loops serem executados sem erros.
Portanto, a estrutura 'for' se aproxima muito da estrutura 'if'
Caso ocorra algum erro na execução da estrutura for, não executam-se
os comandos inclusos em else."""
for x in range(0, 10, 2):
    print(x)
else:
    print('Valores impressos com sucesso')
# Resultado: 0
#            2
#            4
#            6
#            8
#            Valores impressos com sucesso

# ESTRUTURA WHILE
"""Utiliza-se a estrutura while para executar repetida e infinitamente, 
um bloco de comandos enquanto uma dada condição seja verdadeira"""

# Utilizando a estrutura while
"""Ressalta-se que a condição de uma estrutura while deve ter variáveis previamente
inicializadas"""
x = 1
while x <= 5:
    print(x)
    x += 1
# Resultado: 1
#            2
#            3
#            4
#            5

# COMANDOS PARA CONTROLE DE FLUXO
"""Comandos de controle de fluxo permitem controlar ou interromper o fluxo de estruturas de repetições. 
Em Python, existem dois comandos: break e continue. Emprega-se ocomando break para finalizar um laço
de repetição"""
# Aplicando o comando break em uma estrutura for
for x in range(0, 11, 2):
    print(x)
    if x == 8:
        break
# Resultado: 0
#            2
#            4
#            6
#            8

# Aplicando o comando break em uma estrutura while
x = 0
while x < 11:
    print(x)
    x += 2
    if x == 8:
        break
# Resultado: 0
#            2
#            4
#            6

# Aplicando o comando continue em uma estrutura for
"""Aplica-se o comando continue também em estruturas de repetição. Esse comando
interrompe o loop em andamento, executando imediatamente o loop posterior"""
for x in range(0, 11, 2):
    if x == 8:
        continue
    print(x)
# Resultado: 0
#            2
#            4
#            6
#            10

# Aplicando o comando continue em uma estrutura while
x = 2
while x < 11:
    print(x)
    x += 2
    if x == 8:
        continue
# Resultado: 0
#            2
#            4
#            6

# CONTROLE DE ERROS E EXCEÇÕES
"""A linguagem Python gera objetos de erroe os propagam pelo código até que alguma estrutura 
trate-o ou ou paralise a execução doprograma, notificando o programador. Essa notificação 
indica o erro e o local do código, oqual encontra-se o erro. No contexto da programação, 
definem-se erros e exceções. Erros remetem aos problemas funcionais. Enquanto, as exceções
representam ocasiões especiais que possam ocorrer durante a execução do programa. 
Em Python, erros/exceções sãoobjetos de uma classe hierárquica que derivam do tipo BaseException.
As exceções resolvem erros que ocorrem durante a execução do código
    * Exceção: erro gerado durante a execução do programa;
    * Raising an exception: gerando uma exceção;
    * Throwing an exception: acessando uma exceção gerada;
    * Handling an exception: processar código que lida com o erro;
    * Handler: processar código que lida com o erro."""

# LIDANDO COM UMA EXCEÇÃO
"""Em Python, captura-se e trata-se uma exceção por meio da estrutura try-except
• Bloco try: contêm o código que deve ser monitorado para a exceção explicitada no
bloco except ;
• Bloco except: explicita o tipo de erro e contém os comandos para corrigi-lo ou executar outra ação.
Essa estrutura pode ser replicada para capturar diversas exceções;
• Bloco else:contém os códigos que devem ser executados se, e somente se, nenhuma
exceção ocorrer no bloco try;
• Bloco finally: esse bloco é opcional, sendo executado após o bloco try, independentemente se uma 
exceção ocorra."""
# Lidando com excecoes
divisor = float(input('Entre com um numero para dividir:'))
dividendo = 2
try:
    x = dividendo / divisor
    print('Resultado:', x)
except ZeroDivisionError:
    divisor = float(input('Divisao por zero nao e permitida. Informe um numero novamente:'))
    x = dividendo / divisor
    print('Resultado:', x)
else:
    print('O primeiro numero digitado e diferente de zero')
finally:
    print('Divisao com sucesso!')
"""
Resultado: 
        Entre com um numero para dividir:0
        Divisao por zero nao e permitida. Informe um numero novamente:10
        Resultado: 0.2
        Divisao com sucesso!
"""

# Lidando com mutiplas excecoes
indice = int(input('Selecione um indice entre 0 e 2. Esse indice corresponde a um divisor:'))
dividendo = 2
tupla = (0, 1, 2)
try:
    divisor = tupla[indice]
    x = dividendo / divisor
except ZeroDivisionError:
    print('Bad! Você selecionou uma divisao por zero!')
except IndexError:
    print('Indice fora da faixa')
else:
    print('O resultado da divisao e:', x)
finally:
    print('Fim!')
"""
Resultado: 
        Selecione um indice entre 0 e 2. Esse indice corresponde a um divisor:0
        Bad! Você selecionou uma divisao por zero!
        Fim!
"""

# Acessando o objeto de excecao
divisor = float(input('Entre com um numero para dividir:'))
dividendo = 2
try:
    x = dividendo / divisor
    print('Resultado:', x)
except ZeroDivisionError as exp:
    print(exp)
    divisor = float(input('Divisao por zero nao e permitida! Informe um numero novamente:'))
    x = dividendo / divisor
    print('Resultado:', x)
else:
    print('O primeiro numero digitado e diferente de zero')
finally:
    print('Divisao com sucesso!')
"""
Resultado: 
        Entre com um numero para dividir:0
        float division by zero
        Divisao por zero nao e permitida! Informe um numero novamente:12
        Resultado: 0.16666666666666666
        Divisao com sucesso!
"""

# GERANDO UMA EXCEÇÃO
"""Python, pode-se criar ou gerar exceções que são capturadas por blocos 'excep'"""
# Gerando uma excecao
try:
    raise ValueError('Excecao gerada!')
except ValueError as novo:
    print(novo)
# Resultado: Excecao gerada

# EXCEÇÃO CUSTOMIZADA
"""A linguagem Python também permite que o programador defina os próprios erros
e exceções. Para isso, cria-se uma subclasse da classe Exception ou de uma de suas
subclasses"""

# Gerando uma excecao customizada


class NovaExcecao(Exception):
    """Criando uma nova excecao"""


x = 0
try:
    if x == 1:
        print('Ok')
    else:
        raise NovaExcecao("Excecao gerada!")
except NovaExcecao as exp:
    print(exp)
# Resultado: Excecao gerada!

# Relacionando exceções


class NovaExcecao(Exception):
    """Criando uma nova excecao"""
    print('Nova excecao')


y = 1
x = 0
try:
    z = y/x
except Exception as exp:
    print(exp)
    raise NovaExcecao from exp
"""Ao executar esses comandos, verifica-se que a mensagem de erro considera tanto a
exceção generalizada quanto a associada pelo programador"""
