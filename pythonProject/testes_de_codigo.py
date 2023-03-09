def soma(args, **kwargs):  # devolve a soma dos elementos e multiplicação
    s = 0  # parâmetro incial de uma soma de zero elementos
    for cada in args:  # passando em cada valor inserido
        s = s + cada
    print('A soma dos valores é: {}'.format(s))
    s = s * kwargs['chave']
    print('O resultado da multiplicação da soma é: {}'.format(s))


# entrada dos numeros e tranformação do mesmos em uma lista e depois mandados para a função
conjunto = {0}  # elemento inicial do cinjunto
x = int(input('quantidade de numeros a serem somados: '))
for i in range(x):
    y = int(input())
    set.add(conjunto, y)
mult = int(input("Insira o multiplicador: "))
soma(conjunto, chave=mult)
