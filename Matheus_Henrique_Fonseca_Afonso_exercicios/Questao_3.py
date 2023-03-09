def soma(args, **kwargs):  # devolve a soma dos elementos e multiplicação
    s = 0  # parâmetro incial de uma soma de zero elementos
    for cada in args:  # passando em cada valor inserido
        s = s + cada
    print('A soma dos valores é: {}'.format(s))
    s = s * kwargs['chave']
    print('O resultado da multiplicação da soma pelo multiplicador é: {}'.format(s))


# entrada dos numeros e tranformação do mesmos em um conjunto e depois mandados para a função
conjunto = {0}  # elemento inicial do cinjunto
x = int(input('Quantidade de numeros a serem somados: '))
print('Entre com os valores: ')
for i in range(x):
    y = int(input())
    set.add(conjunto, y)
mult = int(input("Insira o multiplicador: "))
soma(conjunto, chave=mult)

"""
RESULTADO:
    Quantidade de numeros a serem somados: 5
    Entre com os valores:
    1
    2
    3
    4
    5
    Insira o multiplicador: 10
    A soma dos valores é: 15
    O resultado da multiplicação da soma pelo multiplicador é: 150
"""
