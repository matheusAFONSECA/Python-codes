# secao de estudos de strings
# uma string e do tipo imutavel, ou seja, nao pode ser mudada depois de definida

# Declarando uma string com aspas simples
palavra_1 = 'ola'
print(palavra_1)

# Declarando strings
Palavra = 'Ola'
print('A string Palavra e do tipo: ', type(Palavra))
# Resultado: A string Palavra e do tipo: <class 'str'>

# Convertendo outros tipos de dados em string
inteiro = str(10)
real = str(1.5)
complexo = str(1 + 2j)
booleano = str(True)
print('A variavel inteiro e do tipo:', type(inteiro))
print('A variavel real e do tipo:', type(real))
print('A variavel complexo e do tipo:', type(complexo))
print('A variavel boooleano e do tipo:', type(booleano))
"""
-> Resultado: A variavel inteiro e do tipo: <class 'str'>
              A variavel real e do tipo: <class 'str'>
              A variavel complexo e do tipo: <class 'str'>
              A variavel booleano e do tipo: <class 'str'>
"""

# Imprimindo uma string
Palavra = 'Estou aprendendo Python'
print(Palavra)
# Resultado: Estou aprendendo Python

# Concatenando strings
Palavra_1 = 'Estou aprendendo '
Palavra_2 = 'Python '
Palavra = Palavra_1 + Palavra_2
print(Palavra)
# Resultado: Estou aprendendo Python
Palavra = Palavra_2 + Palavra_1
print(Palavra)
# Resultado: Python Estou aprendendo

# Multiplicacao com strings
Palavra_1 = 'Oi '
Palavra = Palavra_1 * 3  # a nova string palavra esta sendo feita com tres juncoes de palavra_1
print(Palavra)
# Resultado: Oi Oi Oi

# Acessando caracteres de strings
Palavra = 'Python'
print(Palavra[0])  # observe que as posicoes sao iguais a de vetores,ou seja, comeca no zero
print(Palavra[5])
# Resultado: P
#            n

# Acessando caracteres de strings
Palavra = 'Python'
print(Palavra[-6])  # pode-se usar as posicoes de forma inversa, como os angulos em um circulo trigonometrico
print(Palavra[-1])
# Resultado: P
#            n

# Acessando grupos de caracteres de strings
Palavra = 'Python'
print(Palavra[2:6])  # o pimeiro valor e a posicao primeira e o segundo e ate onde queremos a sequencia
# Resultado: thon

# Determinando o numero de caracteres de uma strings
Palavra = 'Python'
print('A string Palavra possui:', len(Palavra), 'caracteres')  # comando len diz a quantidade de coisas
# Resultado: A string Palavra possui: 6 caracteres

# Metodos para manipulação de String
"""
->Os métodos são funções invocadas por meio da notação de atribuição. 
-> O Python possui uma classe build-in para a manipulação de strings, denominada de str.
-> Essa classe possui diversos métodos, que serão abordados nessa seção.
"""

# Utilizando o metodo str.capitalize()
# O método str.capitalize( ) retorna uma string com o primeiro caractere em maiusculo
# e os demais caracteres em minúsculo
palavra = 'PYTHON'
print(palavra)
resultado = str.capitalize(palavra)
print(resultado)
# Resultado: Python

# Utilizando o metodo str.casefold()
# O método str.casefold( ) retorna uma string com todos os caracteres em minúsculo
palavra = 'PYTHON'
resultado = str.casefold(palavra)
print(resultado)
# Resultado: python

# Utilizando o metodo str.center()
"""
-> O método str.center( ) retorna uma string centralizada em relação a um caractere.
-> Esse método exige dois parâmetros de entrada: o comprimento da string de retorno e
o caractere a ser empregado em ambos os lados dos espaços em brancos da string.
"""
palavra = 'PYTHON'
resultado = palavra.center(12, '*')
print(resultado)
# Resultado: ***PYTHON***

# Utilizando o metodo str.count()
palavra = 'PYTHON'
resultado = palavra.count('P', 0, 5)
print(resultado)
# Resultado: 1
# interfere no resultado se as letras são maiusculas ou minisculas

# Utilizando o metodo str.encode()
palavra = 'Python e massa'
print(palavra.encode(encoding='ascii', errors='backslashreplace'))
print(palavra.encode(encoding='ascii', errors='ignore'))
print(palavra.encode(encoding='ascii', errors='namereplace'))
print(palavra.encode(encoding='ascii', errors='replace'))
print(palavra.encode(encoding='ascii', errors='xmlcharrefreplace'))
"""
-> Demonstram-se os métodos de erros válidos para uma codificação em ASCII
-> Resultado: b'Python \\xe9 m\\xe5ssa'
              b'Python mssa'
              b'Python \\N{LATIN SMALL LETTER E WITH ACUTE} m\\N{LATIN SMALL LETTER A WITH RING ABOVE}ssa'
              b'Python ? m?ssa'
              b'Python &#233; m&#229;ssa']
"""

# Utilizando o metodo str.endswith()
palavra = 'Python'
print(palavra.endswith('on'))
print(palavra.startswith('Py'))
# Resultado: True
#            True
# interfere no resultado se as letras são maiusculas ou minisculas
# lembrando que:
#       -> str.starstwith: analisa o começo da string
#       -> str.endstwith: analisa o começo da string

# Utilizando o metodo str.expandtabs()
palavra = 'P\ty\tt\th\to\tn'  # \t da espaçamento entre as letras
print(palavra)
print(palavra.expandtabs())  # str.expandtabs intensifica o \t, o padrão é 8
print(palavra.expandtabs(10))
"""caso colocado algum numero dentro do parenteses, o espaçamento pode ser maior
                               que o padrão"""
# Resultado: P  y  t  h  o  n
#            P     y     t     h     o     n
#            P       y       t      h        o       n

# Utilizando o metodo str.find()
palavra = 'Python'
resultado = palavra.find('yt')
print(resultado)
# Resultado: 1
# o método retorna o valor ‘1’ caso seja encontrado e ‘-1’ em caso contrário

# Utilizando o metodo str.index()
palavra = 'Python'
resultado = palavra.index('yt')
print(resultado)
# Resultado: 1
# Principio desse metodo é semelhante ao str.find, porém mostra erro quando não encontra o conjunto de caracteres
# que foi pedido

# Utilizando o metodo str.format()
# esse metodo tem três modos de fazer sua aplicação, esses modos são demonstrados abaixo
print('Estou aprendendo {linguagem} e quero aprender {linguagem_1}'.
      format(linguagem='Python', linguagem_1='Java'))
print('Estou aprendendo {0} e quero aprender {1}'.format('Python', 'Java'))
print('Estou aprendendo {} e quero aprender {}'.format('Python', 'Java'))
# Resultado: Estou aprendendo Python e quero aprender Java
# Estou aprendendo Python e quero aprender Java
# Estou aprendendo Python e quero aprender Java

# Utilizando o metodo str.format()
palavra = 'python3'
print(palavra.isalnum())
# Resultado: True
# são várias as funções que podemos usar para saber o conteudo de uma string, há uma tabela com todos na apostila
# de apoio

# Utilizando o metodo str.join()
tupla = ('John', 'Peter', 'Vicky')
separador1 = '−'
resultado1 = separador1.join(tupla)
separador2 = ' * '
resultado2 = separador2.join(tupla)
print('exemplo_1: ', resultado1)
print('exemplo_2: ', resultado2)
# Resultado: exemplo_1:  John−Peter−Vicky
#            exemplo_2:  John * Peter * Vicky

# Utilizando o metodo str.ljust()
# retona a justificativa da string para a esquerda
palavra = 'Python'
resultado = str.ljust(palavra, 20, '*')
print(resultado)
# Resultado: Python**************

# Utilizando o metodo str.rjust()
# retona a justificativa da string para a direita
palavra = 'Python'
resultado = str.rjust(palavra, 20, '*')
print(resultado)
# Resultado: **************Python

# Utilizando os metodos str.lower(), str.upper() e str.swapcase()
palavra = 'PyTHon'
print('exemplo_1: ', str.lower(palavra))
print('exemplo_2: ', str.upper(palavra))
print('exemplo_3: ', str.swapcase(palavra))
print('exemplo_4: ', str.title('python'))
# Resultado: exemplo_1:  python
#            exemplo_2:  PYTHON
#            exemplo_3:  pYthON
#            exemplo_4:  Python

# Utilizando os metodos str.maketrans() e str.translate()
palavra = 'Ola Mara!'
tabela = palavra.maketrans('M', 'S')
print(palavra.translate(tabela))
# Resultado: Ola Sara!

# Utilizando os metodos str.partition() e str.rpartition()
palavra = 'Olá, Sara.Tudo bem, Sara?!'
print(str.partition(palavra, 'Sara'))  # separa da esquerda para a direita
print(str.rpartition(palavra, 'Sara'))  # separa da direita para a esquerda
# Resultado: ('Ola, ', 'Sara', '.Tudo bem, Sara?!')
#            ('Ola, Sara.Tudo bem, ', 'Sara', '?!')

# Utilizando os metodos str.split() e str.rsplit()
palavra = 'Olá Sara. Tudo bem, Sara?!'
print(str.split(palavra, ' ', 2))  # separa da esquerda para a direita
print(str.rsplit(palavra, ' ', 2))  # separa da direita para a esquerda
# Resultado: ['Ola', 'Sara.', 'Tudo bem, Sara?!']
#            ['Ola Sara. Tudo', 'bem,', 'Sara?!']

# Utilizando o metodo str.splitlines()
palavra = 'Hoje eu fui a feira \n. Comprei duas bananas'
# \n pula 4 espaços
print(str.splitlines(palavra, True))  # adiciona o \n
print(str.splitlines(palavra, False))  # não adiciona o \n
# Resultado: ['Hoje eu fui a feira \n.', ' Comprei duas bananas']
#            ['Hoje eu fui a feira.', ' Comprei duas bananas']]

# Utilizando os metodos str.strip() e str.rstrip()
palavra = '****AA**Python**AA****'
print(str.strip(palavra, '*A'))  # remove de ambos os lados
print(str.rstrip(palavra, '*A'))  # remove apenas do lado direito da string
print(str.lstrip(palavra, '*A'))  # remove apenas do lado esquerdo da string
# Resultado: Python
#            ****AA**Python
#            Python**AA****

# Utilizando o metodo str.zfill()
palavra = 'Python'
print(str.zfill(palavra, 6))  # preenche os espaços vazios com 0
print(str.zfill(palavra, 10))
# Resultado: Python
#            0000Python
