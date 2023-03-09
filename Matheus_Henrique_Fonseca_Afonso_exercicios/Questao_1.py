def soma(s=2.5):  # função com parametro padrao e que realiza a soma de duas parcelas, sendo uma definida pelo usuario
    x = float(input('Valor a ser somado: '))
    print('O primeiro valor é: ', s)
    print('O segundo valor é: ', x)
    return s + x


z = soma()
print('A soma dos valores é: ', z)

"""
RESULTADO: 
    Valor a ser somado: 7
    O primeiro valor é:  2.5
    O segundo valor é:  7.0
    A soma dos valores é:  9.5
"""