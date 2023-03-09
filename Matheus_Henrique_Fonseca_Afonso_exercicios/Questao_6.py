class Pessoa:  # superclasse que guarda o nome, idade e altura

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    @property
    def n(self):
        return self.nome

    @property
    def i(self):
        return self.idade

    @i.setter
    def i(self, nova_idade):
        if (0 <= nova_idade <= 100) and isinstance(nova_idade, int):
            self.idade = nova_idade

    def ano_nascimento(self):
        x = int(input('Em que anos estamos?')) - self.idade
        return print('{}, voce nasceu em {}'.format(self.nome, x))


class dados(Pessoa):  # subclasse que guarda o RG e CPF de uma pessoa

    def __init__(self, nome, idade, altura, cpf, rg):
        super().__init__(nome, idade, altura)
        self.cpf = cpf
        self.rg = rg

    def ano_nascimento(self):  # função que devovle os dados da classe pai e do ano de nascimento
        x = int(input('Em que anos estamos? ')) - self.idade
        return print('{}, sua idade é {} anos, voce nasceu em {} e tem {} m'.format(self.nome, self.idade, x, self.altura))


# entrada de dados de uma pessoa
nome_pessoa = str(input('Qual o seu nome: '))
idade_pessoa = int(input('Qual a sua idade: '))
altura_pessoa = float(input('Qual a sua altura: '))
cpf_pessoa = str(input('Qual o seu CPF: '))
rg_pessoa = str(input('Qual o seu RG: '))
pessoa = dados(nome_pessoa, idade_pessoa, altura_pessoa, cpf_pessoa, rg_pessoa)
dados.ano_nascimento(pessoa)
print('Portador(a) do CPF n° {} e RG n° {}'.format(pessoa.cpf, pessoa.rg))

"""
RESULTADO:
    Qual o seu nome: Matheus Fonseca
    Qual a sua idade: 19
    Qual a sua altura: 1.75
    Qual o seu CPF: 1414145673
    Qual o seu RG: MG-20208920
    Em que anos estamos?2022
    Matheus Fonseca, sua idade é 19 anos, voce nasceu em 2003 e tem 1.75 m
    Portador(a) do CPF n° 1414145673 e RG n° MG-20208920
"""
