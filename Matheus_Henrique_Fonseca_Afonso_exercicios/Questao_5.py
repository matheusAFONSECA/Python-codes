def primo(x, d=0):  # Função que determina se um numero é primo ou não
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


# Entrada de um numero para avaliar se o mesmo é primo ou não
z = int(input('Entre com o numero: '))

# chamada de função e saida de dados na função
primo(z)

"""
RESULTADO:
1° CASO: 
    Entre com o numero: 59
    O numero 59 e primo
2° CASO:
    Entre com o numero: 51
    O numero 51 nao e primo
"""
