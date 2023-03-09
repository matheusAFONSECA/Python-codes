fator1 = lambda a, b: a*b  # função anonima que multiplica um numero por outro, ambos definidos pelo usuário
fator2 = lambda a, c: a*c  # função anonima que multiplica um numero por outro, ambos definidos pelo usuário

# Entrada do valor que será multiplicado
valor = int(input('Entre com o valor de um numero: '))

# Entrada do valores que irao multiplicar o primeiro valor entrado
valor_2 = int(input('Entre com o primeiro valor para multiplicar: '))
valor_3 = int(input('Entre com o segundo valor para multiplicar: '))

# Saida da multiplicação
print(valor, ' X ', valor_2, ' = ', fator1(valor, valor_2))
print(valor, ' X ', valor_3, ' = ', fator1(valor, valor_3))

"""
RESULTADO: 
    Entre com o valor de um numero: 2
    Entre com o primeiro valor para multiplicar: 7
    Entre com o segundo valor para multiplicar: 12
    2  X  7  =  14
    2  X  12  =  24
"""