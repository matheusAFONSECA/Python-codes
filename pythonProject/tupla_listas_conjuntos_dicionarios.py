# secao de estudos de tuplas, listas, conjuntos e dicionarios

# TUPLAS

# Declarando uma tupla
tupla_1 = (1, 2, 3)
tupla_2 = tuple((1, 'oi'))
print(type(tupla_1))
print(type(tupla_2))
# Resultado: <class 'tuple'>
#            <class 'tuple'>

# Declarando uma tupla com um unico elemento
tupla = (1,)
print(type(tupla))
# Resultado: <class 'tuple'>

# Acessando itens de uma tupla
tupla = (1, 2, 3)
print('tupla: ', tupla)
print('tupla[0]: ', tupla[0])
print('tupla[1]: ', tupla[1])
print('tupla[2]: ', tupla[2])
"""
tupla:  (1, 2, 3)
tupla[0]:  1
tupla[1]:  2
tupla[2]:  3
"""

# Atribuindo o conteudo de uma tupla para diversas variaveis
tupla = (1, 2, 3)
(a, b, c) = tupla
print(a, b, c)
# Resultado: 1 2 3

# METODOS PARA USAR AS TUPLAS

# Utilizando o metodo tuple.count( )
tupla = (1, 2, 1)
print(tuple.count(tupla, 1))
# Resultado: 2

# Utilizando o metodo tuple.index( )
tupla = (1, 2, 1)
print(tuple.index(tupla, 1))  # retorna posição do número procurado
# caso não tenha o número na tupla, retorna nada
# Resultado: 0

# Determinando a quantidade de elementos de uma tupla
tupla = (1, 2, 1)
print(len(tupla))
# Resultado: 3

# LISTAS

# Declarando uma lista
lista_1 = [1, 2, 3]
lista_2 = list([1, 2, 2])
print(type(lista_1))
print(type(lista_2))
# Resultado: <class 'list'>
#            <class 'list'>

# Acessando itens de uma lista
lista = [1, 2, 3]
print('lista: ', lista)
print('lista[0]: ', lista[0])
print('lista[1]: ', lista[1])
print('lista[2]: ', lista[2])
"""
Resultados:
    lista:  [1, 2, 3]
    lista[0]:  1
    lista[1]:  2
    lista[2]:  3
"""

# Modificando elementos de uma lista
lista = [1, 2, 3]
lista[0] = 3
print(lista)
# Resultado: [3, 2, 3]

# METODOS PARA USAR AS LISTAS

# Utilizando o metodo list.append( )
lista = [1, 2, 3]
list.append(lista, 4)  # só pode ser adicionado um elemento
print(lista)
# adiciona um elemento a lista
# Resultado: [1, 2, 3, 4]

# Utilizando o metodo list.clear( )
# metodo que apaga tudo da lista
lista = [1, 2, 3]
list.clear(lista)
print(lista)
# Resultado: []

# Utilizando o metodo list.copy( )
lista = [1, 2, 3]
lista_copiada = list.copy(lista)  # faz uma cópia da lista
print(lista_copiada)
# Resultado: [1, 2, 3]

# Utilizando o metodo list.count( )
lista = [1, 2, 3]
print(list.count(lista, 1))
# Resultado: 1

# Utilizando o metodo list.extend( )
lista = [1, 2, 3]
lista_2 = [4, 5]
list.extend(lista, lista_2)
print(lista)
list.extend(lista_2, lista_2)
print(lista_2)
list.extend(lista_2, lista)
print(lista_2)
# Resultado: [1, 2, 3, 4, 5]
#            [4, 5, 4, 5]
#            [4, 5, 4, 5, 1, 2, 3, 4, 5]

# Utilizando o metodo list.index( )
lista = [1, 2, 1]
print(list.index(lista, 2))
# Resultado: 1

# Utilizando o metodo list.insert( )
lista = [1, 2, 1]
list.insert(lista, 1, 'oi')  # não é bom colocar uma str em uma lista com elementos int
# OBS: não é indicado misturar tipos de variável dentro de uma lista
print(lista)
# Resultado: [1, 'oi', 2, 1]

# Utilizando o metodo list.pop( )
lista = [1, 2, 1]
list.pop(lista, 1)  # é possível escolher o indice (posição) do elemento a ser retirado
print(lista)
# Resultado: [1, 1]

# Utilizando o metodo list.remove( )
lista = [1, 2, 1]
list.remove(lista, 2)  # remove o primeiro elemento encontrado com esse valor
# caso não tenha o elemento na lista, da erro de execução
print(lista)
# Resultado: [1, 1]

# Utilizando o metodo list.reverse( )
lista = [1, 2, 3]
list.reverse(lista)
print(lista)
# Resultado: [3, 2, 1]

# Utilizando o metodo list.sort( )
lista = [1, 3, 2]
list.sort(lista)
print(lista)
# Resultado: [1, 2, 3]

# CONJUNTOS

# Declarando um set
conjunto_1 = {1, 2, 3}
conjunto_2 = set({1, 2, 2})
print('conjunto_1 = ', conjunto_1)
print(type(conjunto_1))
print('conjunto_2 = ', conjunto_2)
print(type(conjunto_2))
# Resultado: conjunto_1 =  {1, 2, 3}
#            <class 'set'>
#            conjunto_2 =  {1, 2}   ->  observe que elmentos repetidos são colocados somente um
#            <class 'set'>

# Verificando se um elemento esta presente em um set
conjunto = {1, 2, 3}
print('conjunto = ', conjunto)
print(1 in conjunto)
print(5 in conjunto)
# Resultado: True
#            False

# METODOS PARA USAR OS CONJUNTOS

# Utilizando o metodo set.add( )
conjunto = {1, 2, 3}
set.add(conjunto, 4)  # adiciona o segundo parâmetro para o conjunto
print(conjunto)
# Resultado: {1, 2, 3, 4}

# Utilizando o metodo set.clear( )
conjunto = {1, 2, 3}
set.clear(conjunto)  # limpa todos os elementos do conjuto
print(conjunto)
# Resultado: set()

# Utilizando o metodo set.copy( )
conjunto = {1, 2, 3}
conjunto_copiado = set.copy(conjunto)  # copia o conjunto para outro
print(conjunto_copiado)
# Resultado: {1, 2, 3}

# Utilizando o metodo set.difference( )
conjunto_1 = {1, 2, 3}
conjunto_2 = {1, 4, 3}
print(set.difference(conjunto_1, conjunto_2))
print(set.difference(conjunto_2, conjunto_1))
# Mostra um conjunto com a diferança entre o conjunto do primeiro parâmetro em relação ao segundo parâmetro
# Resultado: {2}
#            {4}

# Utilizando o metodo set.difference\_update( )
conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {1, 4, 3, 5}
print('conjunto_1 = ', conjunto_1)
print('conjunto_2 = ', conjunto_2)
set.difference_update(conjunto_1, conjunto_2)
print(conjunto_1)
conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {1, 4, 3, 5}
set.difference_update(conjunto_2, conjunto_1)
print(conjunto_2)
# Resultado: {2}
#            {5}

# Utilizando o metodo set.discard( )
conjunto = {1, 2, 3, 4}
set.discard(conjunto, 2)  # discarta um elemento específico
print(conjunto)
# Resultado: {1, 3, 4}

# Utilizando o metodo set.intersection( )
conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {1, 4, 3, 5}
print(set.intersection(conjunto_1, conjunto_2))
# mostra a interseção de elementos ente dois conjuntos
# Resultado: {1, 3, 4}

# Utilizando o metodo set.intersection\_update( )
conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {1, 4, 3, 5}
set.intersection_update(conjunto_1, conjunto_2)
print(conjunto_1)
# Resultado: {1, 3, 4}

# Utilizando os metodos set.isdisjoint( ), set.issubset( ) e set.issuperset( )
conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {5, 6}
print(set.isdisjoint(conjunto_1, conjunto_2))
print(set.issubset(conjunto_1, conjunto_2))
print(set.issuperset(conjunto_1, conjunto_2))
# Resultado: True
#            False
#            False

# Utilizando os metodos set.pop( )
conjunto = {1, 2, 3, 4}
elemento_removido = set.pop(conjunto)
# .pop remove algum elemento aleatório e pode atribuir a algum elemento
print('conjunto = ', conjunto)
print('elemento_removido = ', elemento_removido)
# Resultado: conjunto =  {2, 3, 4}
#            elemento_removido =  1

# Utilizando o metodo set.remove( )
conjunto = {1, 2, 3, 4}
set.remove(conjunto, 4)
print(conjunto)
# Resultado: {1, 2, 3}

# Utilizando os metodos set.symmetric_difference( ) e set.symmetric_difference_update( )
conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {5, 6}
print(set.symmetric_difference(conjunto_1, conjunto_2))
set.symmetric_difference_update(conjunto_1, conjunto_2)
print(conjunto_1)
# Resultado: {1, 2, 3, 4, 5, 6}
#            {1, 2, 3, 4, 5, 6}

# Utilizando os metodos set.union( ) e set.update( )
conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {4, 5, 6}
print(set.union(conjunto_1, conjunto_2))
set.update(conjunto_1, conjunto_2)
print(conjunto_1)
# Resultado: {1, 2, 3, 4, 5, 6}
#            {1, 2, 3, 4, 5, 6}

# DICIONARIOS

# Declarando um dicionario
dicionario_1 = {'a': 1, 'b': 2, 'c': 3}
dicionario_2 = dict({'a': 1, 'b': 2, 'c': 3})
print('dicionario_1 = ', dicionario_1, ' -> ', type(dicionario_1))
print('dicionario_2 = ', dicionario_2, ' -> ', type(dicionario_2))
# Resultado: dicionario_1 =  {'a': 1, 'b': 2, 'c': 3}  ->  <class 'dict'>
#            dicionario_2 =  {'a': 1, 'b': 2, 'c': 3}  ->  <class 'dict'>

# Acessando itens de um dicionario
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dicionario['a'], dicionario['b'], dicionario['c'])
# Resultado: 1 2 3

# Modificando elementos de um dicionario
dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario1['a'] = 10
print(dicionario1)
# Resultado: {'a': 10, 'b': 2, 'c': 3}

# Adicionando elementos de um dicionario
dicionario = {'a': 1, 'b': 2, 'c': 3}
dicionario['d'] = 10
print(dicionario)
# Resultado: {'a': 1, 'b': 2, 'c': 3, 'd': 10}

# METODOS PARA USAR OS DICIONARIOS

# Utilizando o metodo dict.clear( )
dicionario = {'a': 1, 'b': 2, 'c': 3}
dict.clear(dicionario)
print(dicionario)
# Resultado: {}

# Utilizando o metodo dict.copy( )
dicionario = {'a': 1, 'b': 2, 'c': 3}
dicionario_1 = dict.copy(dicionario)
print(dicionario_1)
# Resultado: {'a': 1, 'b':2, 'c':3}

# Utilizando o metodo dict.fromkeys( )
chaves = ('a', 'b', 'c')
valor = 1
dicionario = dict.fromkeys(chaves, valor)
print(dicionario)
# Resultado: {'a': 1, 'b': 1, 'c': 1}

# Utilizando o metodo dict.get( )
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dict.get(dicionario, 'a'))
# Resultado: 1

# Utilizando o metodo dict.items( )
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dict.items(dicionario))
# Resultado: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Utilizando o metodo dict.keys( )
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dict.keys(dicionario))
# Resultado: dict_keys(['a', 'b', 'c'])

# Utilizando o metodo dict.pop( )
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dict.pop(dicionario, 'a'))
print(dicionario)
# Resultado: 1
#            {'b': 2, 'c': 3}

# Utilizando o metodo dict.popitem( )
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dict.popitem(dicionario))
print(dicionario)
# Resultado: ('c', 3)
#            {'a': 1, 'b': 2}

# Utilizando o metodo dict.setdefault( )
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dict.setdefault(dicionario, 'd', 3))
print(dicionario)
# Resultado: 3
#            {'a': 1, 'b': 2, 'c': 3, 'd': 3}

# Utilizando o metodo dict.update( )
dicionario = {'a': 1, 'b': 2, 'c': 3}
dict.update(dicionario, {'d': 3})
print(dicionario)
# Resultado: {'a': 1, 'b': 2, 'c': 3, 'd': 3}

# Utilizando o metodo dict.values( )
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dict.values(dicionario))
# Resultado: dict_values([1, 2, 3])
