def soma(s, w):  # função que a faz a soma das parcelas
    s = s + w
    return s


resultado = 0  # porque nada foi somado ainda
# entrada da quantidade de n° a serem somados
x = int(input('Quantidade de numeros a serem somados: '))

# entrada do numeros por meio de um for e soma dos mesmos
print('Entre com os valores: ')
for y in range(x):
    z = float(input())
    resultado = soma(resultado, z)

# Saida do resultado da soma dos valores entrados
print('A soma dos valores é: ', resultado)

"""
RESULTADO:
    Quantidade de numeros a serem somados: 3
    Entre com os valores: 
    6
    4
    10
    A soma dos valores é:  20.0
"""
