"""
# definição de um função
def func(z=int(input('z=')), y=2):
    return z * y


# z = int(input('Z = '))2
x = func
print(x())

# atribuição de um comando para uma variável
p = print
p(12)
"""

"""def mensagem():
    print('Eu sou a funcao mensagem')


endereco1 = mensagem
print(endereco1)
mensagem()
# Resultado: <function mensagem at 0x0208B808>
#            Eu sou a funcao mensagem"""

'''a, b, c = 1, 2, 3

print(f"{a}, {b}, {c}")'''

'''dicionario = {'a': 1, 'b':2, 'c':3}
dicionario.update({'d': 1, 'e':2, 'f':3})
print(dicionario)'''

"""def func(arg, **kwarg):
    return arg + kwarg["aa"]


print(func(12, aa=10))
"""

import datetime


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def __str__(self):
        return self.nome + 'tem ' + str(self.idade) + ' anos e ' + str(self.altura) + 'm de altura'

    def ano_nascimento(self):
        ano = datetime.date.today().year
        x = ano - self.idade
        return print('{}, voce nasceu em {}'.format(self.nome, x))


pessoa = Pessoa('Ana', 21, 1.8)
pessoa.ano_nascimento()
