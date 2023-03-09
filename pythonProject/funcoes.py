# SEÇÃO DE ESTUDOS SOBRE FUNÇÕES
"""
As funções podem
incluir parâmetros de entrada ou não, assim como retornar um determinado valor ou não.
Declaram-se as funções em qualquer parte do código e as invocam sempre que necessário.
Existem dois tipos de funções: funções build-in e definidas pelo usuário.
As funções build-in integram o núcleo da linguagem Python.
Já as funções definidaspelo usuário não pertencem ao núcleo da linguagem, sendo definidas pelo usuário sob
demanda para um programa especifico.

"""

# DECLARANDO UMA FUNÇÃO
"""
Toda e qualquer função definida por um usuário deve empregar a palavra-chave 'def'.
Os parâmetros de entrada representam variáveis que receberão valores, em alguns 
casos necessários, para que afunção execute a rotina.
Emprega-se o símbolo ‘:’ para indicar o fim da definição de uma função e o início dos comandos.
Para funções que retornam um determinado tipo de dado,
emprega-se a palavra-chave return seguida da varáivel que armazena o valor.
"""


# Exemplo de uma funcao


def imprimir(texto):
    print(texto)


menssagem = input('Digite uma mensagem:')
imprimir(menssagem)


# Resultado: Ola, estou aprendendo Python

# TIPOS DE FUNÇÃO

# Exemplo de uma funcao com parametro de entrada e retorno


def soma(a, b):
    c = a + b
    return c


numero_1 = int(input('Digite um numero:'))
numero_2 = int(input('Digite um segundo numero:'))
numero_soma = soma(numero_1, numero_2)
print('A soma de {} e {} e igual a {}'.format(numero_1, numero_2, numero_soma))
# Resultado: A soma de 1 e 2 e igual a 3
""" A variável ‘c’ é de escopo local, ou seja, pode ser acessada somente pela função soma( ),
pois a declarou dentro dessa função"""

"""Reescreve-se esse exemplo para demonstrar uma função sem parâmetro de entrada e
com retorno"""


# Exemplo de uma funcao sem parametro de entrada e com retorno


def soma():
    a = int(input('Digite um numero:'))
    b = int(input('Digite um segundo numero:'))
    c = a + b
    return a, b, c


resultado = soma()
print('A soma de {} e {} e igual a {}'.format(resultado[0], resultado[1], resultado[2]))
# Resultado: A soma de 1 e 2 e igual a 3

"""No exemplo a seguir, mantém-se osparâmetros de entrada e remove-se o retorno da função"""


# Exemplo de uma funcao com parametro de entrada e sem retorno


def soma(a, b):
    c = a + b
    print('A soma de {} e {} e igual a {}'.format(a, b, c))


numero_1 = int(input('Digite um numero:'))
numero_2 = int(input('Digite um segundo numero:'))
soma(numero_1, numero_2)
# Resultado: A soma de 1 e 2 e igual a 3

"""Por fim, reescreve-se o exemplo para declaração de uma função sem parâmetros de
entrada e sem retorno"""


# Exemplo de uma funcao sem parametro de entrada e retorno


def soma():
    a = int(input('Digite um numero:'))
    b = int(input('Digite um segundo numero:'))
    c = a + b
    print('A soma de {} e {} e igual a {}'.format(a, b, c))


soma()


# Resultado: A soma de 1 e 2 e igual a 3

# FUNÇÃO COM PARAMETRO PADRÃO

# Exemplo de uma funcao com parametro padrao


def soma(a=3):
    b = int(input('Digite um numero:'))
    c = a + b
    print('A soma de {} e {} e igual a {}'.format(a, b, c))


soma()


# Resultado: A soma de 3 e 1 e igual a 4

# Exemplo de uma funcao com parametro padrao que é mudado ao chamar a função


def soma(a=3):
    b = int(input('Digite um numero:'))
    c = a + b
    print('A soma de {} e {} e igual a {}'.format(a, b, c))


soma(a=4)
# Resultado: A soma de 4 e 1 e igual a 5

# FUNÇÃO COM PARÂMETROS ARBITRARIOS
"""Para algumas funções não há como definir a quantidade de parâmetros de entrada.
Nesse caso, a linguagem Python permite declarar funções com parâmetros arbitrários."""


# Exemplo de uma funcao com parametros arbitrarios


def soma(*a):
    c = 0
    for x in a:
        c += x
    print('A soma desses numeros e:', c)


soma(1, 2, 3)
soma(1, 2)
# Resultado: A soma desses numeros e: 6
#            A soma desses numeros e: 3
"""poranto, ao declarar uma função arbitrária podemos utilizar vários valores"""

# FUNÇÃO COM PARAMETROS POSICIONAIS E PALAVRAS-CHAVES
""" Indicam-se os parâmetros posicionais usando o símbolo ‘*’ no momento 
da declaração da função. 
Para os parâmetros palavra-chave, empregam-se o símbolo ‘**’"""


# Exemplo de uma funcao com parametro posicional e palavra−chave


def soma(*a, **b):
    c = 0
    for x in a:
        c += x
    print('A soma desses numeros e:', c)
    print('A soma multiplicada por', b['multiplicador'], 'e:', (c * b['multiplicador']))


soma(1, 2, 3, multiplicador=3)
# Resultado: A soma desses numeros e: 6
#            A soma multiplicada por 3 e: 18

# FUNÇÃO ANÔNIMA OU LAMBDA
"""Existem funções em Python que são utilizadas apenas no momento da declaração e
não podem ser reutilizadas em outros momentos. 
Essas funções não possuem nomes e, portanto, denominam-nas de funções anônimas ou lambda. 
Pois utiliza-se a palavra-chave ‘lambda’ para declará-las. """

# Exemplo de funcao lambda


soma = lambda a, b: a + b


print('A soma de {} e {} e: {}'.format(1, 2, soma(1, 2)))
# Resultado: A soma de 1 e 2 e:

# Exemplo de uma aplicacao de funcao lambda


def multiplica(x):
    return lambda n: n*x


multiplica_2 = multiplica(2)
multiplica_3 = multiplica(3)

print(multiplica_2(3))
print(multiplica_3(3))
# Resultado: 6
#            9

# RECURSÃO
""" Uma solução recursiva em uma linguagem de programação refere-se
à funções que se auto invocam uma ou várias vezes para solucionar um dado problema,
sendo definidas como funções recursivas"""

# Exemplo de uma funcao recursiva para verificar se um numero e primo


def primo(x, d=0):
    tupla = (2, 3, 5, 7)
    if (d < 4) and (x != 1):
        if (x % tupla[d] != 0) or (x in tupla):
            primo(x, d=d+1)
        else:
            return print('O numero {} nao e primo'.format(x))
    elif x != 1:
        return print('O numero {} e primo'.format(x))
    else:
        return print('O numero {} nao e primo'.format(x))


print(primo(10103))
# Resultado: O numero 10103 e primo

# VARIÁVEIS GLOBAL E LOCAL NO CONTEXTO DE FUNÇÕES
""" Já as variáveis de uso restrito por umafunção correspondem as variáveis de escopo local. 
Inicializam-se essas variáveis dentro das funções correspondentes.
No exemplo a seguir, manipulase uma variável global e local de mesmo nome e imprime-se o conteúdo de ambas"""

# Manipulando variaveis global e local no contexto de funcoes
mensagem = 'Eu sou uma variavel global'


def imprime():
    mensagem = 45
    print(mensagem)


imprime()
print(mensagem)

# Resutaldo: Eu sou uma variavel local
#            Eu sou uma variavel global
"""Ao executar o código, as variáveis mantêm seus respectivos textos. Isso ocorre pois o Python
distingue variáveis de acordo com o escopo"""

# Manipulando variaveis global e local no contexto de funcoes
mensagem = 'Eu sou uma variavel global'


def imprime():
    print(mensagem)


imprime()
print(mensagem)
# aqui a variável global foi usada tanto para a função quanto para o escopo principal
# Resutaldo: Eu sou uma variavel global
#            Eu sou uma variavel global

""".Em um segundo cenário, se a variável mensagem não for declarada em escopo
global, o programa não consegue acessar a variável mensagem de escopo local por meio
de linhas de códigos que não estejam contidas na função imprime( )"""

# Manipulando variaveis global e local no contexto de funcoes


def imprime():
    mensagem = 'Ola, eu sou uma variavel local'
    print(mensagem)


imprime()
print(mensagem)  # linha de comando que gera o erro uma vez que não foi declarado nesse escopo
# o 'valor' da variável 'mensagem'
# Resutaldo: Ola, eu sou uma variavel local
#            NameError: name 'variavel' is not defined

"""
Resolve-se essa situação tornando a variável mensagem de escopo local em uma variável
de escopo global, mantendo a declaração interna à função imprime( ). Isso é possível por 
meio da palavra-chave 'global'
"""

# Manipulando variaveis global e local no contexto de funcoes


def imprime():
    global mensagem  # assim que transforma a variável local em global
    mensagem = 'Ola, eu sou uma variavel global declarada em uma funcao'
    print(mensagem)


imprime()
print(mensagem)
# Resutaldo: Ola, eu sou uma variavel global declarada em uma funcao
# Ola, eu sou uma variavel global declarada em uma funcao

"""Logo, a função interna não pode modificar o valor de uma variável local a função
que a contém. 
Caso faça, entende-se como uma nova variável sendo declarada e com nome comum a da primeira.
Contorna-se essa situação utilizando uma segunda palavrachave, a nonlocal. 
Essa palavra-chave permite que uma função interna a outra modifique uma variável"""

# Manipulando variaveis locais no contexto de funcoes


def imprime():
    mensagem = 'Eu sou uma variavel local da funcao imprime( )'

    def imprime_2():
        nonlocal mensagem
        mensagem = 'Eu sou uma variavel local da funcao imprime_2( )'
        print(mensagem)

    print(mensagem)
    imprime_2()


imprime()
# Observe que para separa uma função dentro de outra devemos usar uma linha para separá-las
# Resutaldo: Eu sou uma variavel local da funcao imprime( )
#            Eu sou uma variavel local da funcao imprime_2( )

# FUNÇÕES COMO OBJETOS
"""o nome dado a uma função constitui um objeto que armazena o seu endereço de memória, assim
como uma variável qualquer armazena o endereço de memória de um dado"""

# Descobrindo o endereco de memoria de uma funcao


def mensagem():
    print('Eu sou a funcao mensagem')


endereco = mensagem
print(endereco)
# Resultado: <function mensagem at 0x0208B808>

# A seguir mostra a diferença de acessar o endereço de memória e de chamar a função como um obejeto

# Descobrindo o endereco de memoria de uma funcao


def mensagem():
    print('Eu sou a funcao mensagem')


endereco1 = mensagem
print(endereco1)
mensagem()
# Resultado: <function mensagem at 0x0208B808>
#            Eu sou a funcao mensagem

# Manipulando funcao como objeto


def mensagem():
    print('Eu sou a funcao mensagem')


endereco = mensagem
endereco()
# aqui tranformou-se a função em objeto e depois usou ela com o nome da variável que a definiu como objeto
# Resultado: Eu sou a funcao mensagem

"""Ressalta-se que ambos os objetos
mensagem e endereco podem acessar e executar os comandos da função"""

# Manipulando funcao como objeto


def mensagem():
    print('Eu sou a funcao mensagem')


endereco = mensagem
mensagem()
endereco()
# Resultado: Eu sou a funcao mensagem
#            Eu sou a funcao mensagem

# FUNÇÕES DE ALTA ORDEM
""" uma função pode ter como argumento a referência de uma segunda função e/ou retornar uma terceira função.
Denomina-se a primeira função como uma função de alta ordem"""

# Exemplo de funcao de alta ordem


def multiplicar(a):
    return a*10


def somar(b, funcao):
    c = b + funcao(4)
    return c


resultado = somar(2, multiplicar)
print(resultado)
# Resultado: 42

# Exemplo de funcao de alta ordem


def operacao(a):
    if a == 1:
        return lambda n: n*10
    elif a == 2:
        return lambda n: n+10
    else:
        return lambda n: n-10


valor_1 = operacao(1)
valor_2 = operacao(2)
valor_3 = operacao(3)

print(valor_1(2))
print(valor_2(2))
print(valor_3(2))
# Resultado: 20
#            12
#            −8
