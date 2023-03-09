# secao de estudos dos tipos de dados
""""
-> Tipos de dados: utilizados para especificar o espaço de memória reservado para
armazenar o dado, a forma como se deve interpretar o código binário e as operações que
podem ou não ser aplicadas sobre o dado, divididos em duas categprias:
        -> PRIMITIVOS SIMPLES: números (int, float, complex) e booleanos (true ou false);
        -> PRIMITIVOS COMPOSTOS: cadeias de caracteres (string), listas, dicionários, tuplas e conjuntos.
-> Serão mostrados, em um primeiro momento, dados do tipo primitivo simples.
"""

# VARIAVEIS DO TIPO NUMEROS REAIS, INTEIROS, COMPLEXOS E COMPLEXOS

# Declarando uma variavel do tipo inteiro
inteiro = 3
print('A variavel inteiro e do tipo:', type(inteiro))  # type comando que diz qual o tipo da variavel
# Resultado: A variavel e do tipo: <class `int'>

# Convertendo uma string em um numero inteiro
inteiro = int('10')
print('Converteu−se a string 10 no inteiro 10, a variavel inteiro e do tipo:', type(inteiro))
"""
-> Resultado: Converteu−se a string 10 no inteiro 10, a variavel inteiro e do tipo: <class 'int'>
-> Ressalta-se que para parâmetros de entrada do tipo string, o dado deve representar um número inteiro, caso
contrário, variável tipo float por exemplo, ocorreria a perde de dados, uma vez que seria convertido a parte
inteira somente.
"""

# Declarando uma variavel do tipo real
real = 3.5
print('A variavel reale e do tipo:', type(real))
# Resultado: A variavel e do tipo: <class `float'>

# Convertendo uma string e um inteiro em um numero real
real_1 = float('10.5')
print('real_1: ', real_1)  # Assim que mostramos uma mensagem e logo em seguida um resultado
real_2 = float(10)
print('A variavel real_1 e do tipo:', type(real_1))
print('A variavel real_2 e do tipo:', type(real_2))
""" 
-> Resultado: A variavel real_1 e do tipo: <class `float'>
              A variavel real_2 e do tipo: <class `float'>
-> Ressalta-se que para parâmetros de entrada do tipo string, o dado deve representar um número inteiro ou real.
"""

# Declarando uma variavel do tipo complexo
complexo = 3+1j  # parte complexa respresentada como j, assim como na engenharia
print('A variavel e do tipo:', type(complexo))
# Resultado: A variavel complexo e do tipo: <class `complex'>

# Convertendo um numero inteiro, numero real e uma string em um numero complexo
complexo_1 = complex(10)
complexo_2 = complex(10.5)
complexo_3 = complex('10')
print('A variavel complexo_1 e do tipo:', type(complexo_1))
print('A variavel complexo_2 e do tipo:', type(complexo_2))
print('A variavel complexo_3 e do tipo:', type(complexo_3))
"""
-> Resultado: A variavel complexo_1 e do tipo: <class `complex'>
              A variavel complexo_2 e do tipo: <class `complex'>
              A variavel complexo_3 e do tipo: <class `complex'>
"""

# Declarando variaveis do tipo booleano
verdadeiro = True
falso = False
print('A variavel verdadeiro e do tipo:', type(verdadeiro))
print('A variavel falso e do tipo:', type(falso))
"""
-> Resultado: A variavel verdadeiro e do tipo: <class 'bool'>
              A variavel falso e do tipo: <class 'bool'>
-> Observe que temos que fazer a atribuição True e False com as primeiras letras maiusculas para haver efeito, 
sendo que ao colocar true e false criamos nomes de variáveis e nao uma atribuição booleana
-> Em termos numéricos, o valor True corresponde a qualquer valor diferente de zero,que é representado por False.
-> Em relação as strings, associa-se qualquer caractere ao valor True e espaço (nenhum caractere) ao valor False. 
-> Portanto o False representa a falta de algo ou o nada e o True é o oposto disso.
"""

# Convertendo outros tipos de dados em booleano
inteiro = bool(10)
real = bool(1.5)
complexo = bool(1+2j)
caractere = bool('A')
false1 = bool(0)
print(inteiro)
print('A variavel inteiro e do tipo:', type(inteiro))
print(real)
print('A variavel real e do tipo:', type(real))
print(complexo)
print('A variavel complexo e do tipo:', type(complexo))
print(caractere)
print('A variavel caractere e do tipo:', type(caractere))
print(false1)
print('A variavel false1 e do tipo:', type(false1))
"""
-> Resultado: True
              A variavel inteiro e do tipo: <class 'bool'>
              True
              A variavel real e do tipo: <class 'bool'>
              True
              A variavel complexo e do tipo: <class 'bool'>
              True
              A variavel caractere e do tipo: <class 'bool'>
              False
              A variavel caractere e do tipo: <class 'bool'>
"""

# OPERADORES

# Explorando os operadores aritmeticos
x = 3
print('x = ', x)
y = 4
print('y = ', y)
print('x+y = ', x + y)  # adicao
print('x-y = ', x - y)  # subtracao
print('x*y = ', x * y)  # multiplicacao
print('x/y = ', x / y)  # divisao
print('x+y = ', x % y)  # resto da divisao nao exata
print('x**y = ', x ** y)  # exponenciacao
print('x//y = ', x // y)  # divisao com arredondamento para baixo
""""
-> Resultado: 7
              −1
              12
              0.75
              3
              81
              0
"""

# Explorando os operadores de atribuicao
x = 1
x += 3  # x soma com 3
print(f'x += 3: {x}')  # f'x += 3: {x}' é o mesmo que escrever 'x += 3', x
x = 1
x -= 3  # x subtrai 3
print(f'x -= 3: {x}')
x = 1
x *= 3  # x multiplica por 3
print(f'x *= 3: {x}')
x = 1
x /= 3  # x divide por 3
print(f'x /= 3: {x}')
x = 1
x %= 3  # resto da divisão de x por 3
print(f'x %= 3: {x}')
x = 1
x //= 3  # atribuição por divisão com arredondamento para baixo de x por 3
print(f'x //= 3: {x}')
x = 1
x **= 3  # exponiação de x por 3
print(f'x **= 3: {x}')
x = 1
x &= 1  # atribuição por relação binária E
print(f'x &= 1: {x}')
x = 1
x |= 3  # atribuição por relação binária OU
print(f'x |= 3: {x}')
x = 1
x ^= 3  # atribuição por relação binária Não OU
print(f'x ^= 3: {x}')
"""
-> Resultado: 4
              −2
              3
              0.333333
              1
              0
              1
              1
              3
              2
"""

# Explorando os operadores de comparacao
x = 1
y = 4
print('x = ', x)
print('y = ', y)
print('x == y :', x == y)  # igualdade
print('x 1= y :', x != y)  # Diferenca
print('x > y :', x > y)  # maior que
print('x < y :', x < y)  # menor que
print('x >= y :', x >= y)  # maior ou igual à
print('x <= y :', x <= y)  # menor ou igual à
"""
-> Resultado: False
              True
              False
              True
              False
              True
"""

# Explorando os operadores logicos
x = 1
y = 4
print(x == 1 and y == 4)
print(x != y or y == 4)
print(not(x == 1 and y == 4))
"""
-> Resultado: True
              True
              False
              
                                        *Operadores lógicos*
    Operador:                                Descrição:                                           Sintaxe:
->    and           Retorna True se ambas as declarações forem verdadeiras                    x == 1 and y == 3
->    or            Retorna True se uma das declarações forem verdadeiras                     x == 1 or y == 3
->    not           Inverte o resultado de uma declaração                                  not(x == 1 and y == 3)
"""

# Explorando os operadores de identidade
x = 1
y = 4
print(x is y)
print(x is not y)
# Resultado: False
#           True

"""
                                *Operadores de identidade*
    Operador:                           Descrição:                                       Sintaxe:
->     is               Retorna True se ambas as variáveis forem o mesmo objeto           x is y
->   is not             Retorna True se as variáveis não forem o mesmo objeto           x is not y
"""

# Explorando os operadores de continencia
x = 1
print(x in [3, 2])
print(x not in [3, 2])
# Resultado: False
#           True
"""
                                    *Operadores de continência*
    Operador:                               Descrição:                                     Sintaxe:
->     in             Retorna True se a variáveis está contida no objeto                    x in y
->   not in           Retorna True se a variáveis não está contida no objeto              x not in y
"""
