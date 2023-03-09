# secao de estudos para orientação a objetos em python e sobre classes
""""
A maioria dos erros que são acusados aqui ocorrem porque tem a declaração sucessiva da mesma classe e obejeto
constantemente, algo que não pode ocorrer no cógigo.
A linguagem de programação Python oferece suporte para a programação orientada a
objetos (POO), cujo conceito refere-se a concepção de códigos reutilizáveis.
A classe é um bloco de construção básico do Python e o núcleo da POO.
Na POO, utilizam-se alguns termos e definições:
    • Classe: template para a criação de objetos ou instâncias. Integra variáveis e funcionalidades que
    operam sobre um determinado dado;
    • Objetos ou instância: são exemplos de uma classe. Todas as instâncias de uma
    classe compartilham os mesmos campos/atributos. Porém, contêm valores ou dados
    diferentes;
    Campos ou atributos: correspondem à estruturas que armazenam os dados de uma
    instância. Em outras palavras, são variáveis declaradas dentro do contexto de uma
    classe;
    Método: corresponde a um conjunto de linhas de código que realizam uma tarefa
    especifica sobre os dados de um objeto ou instância.
"""

# DEFINIÇÃO DE CLASSES E OBJETOS
# Em Python, considera-se tudo um objeto e, portanto, um exemplo de uma classe

# Declarando uma classe


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura


"""O método __init__ é denotado como um método especial e inicializador, comumente
referenciado como construtor da classe. 
Esse método especifica quais são os valores que devem ser passados como argumento para a classe no 
momento em que se cria um objeto ou instância, assim como deve-se armazenar esses valores em campos.
A palavra-chave self representa uma campo especial e corresponde ao primeiro parâmetro de cada método. 
Essa variável permite que o método acesse os dados contidos pelo objeto."""

# Criando objetos para a classe Pessoa
objeto_1 = Pessoa('Ana', 18, 1.7)
objeto_2 = Pessoa('Joao', 25, 1.8)

# Acessando dados de um objeto
print('{} tem {} anos e {}m de altura'.format(objeto_1.nome, objeto_1.idade, objeto_1.altura))
print('{} tem {} anos e {}m de altura'.format(objeto_2.nome, objeto_2.idade, objeto_2.altura))
# Resultado: Ana tem 18 anos e 1.7m de altura
#            Joao tem 25 anos e 1.8m de altura

# Manipulando objetos de uma classe
objeto_1 = Pessoa('Ana', 18, 1.7)
objeto_3 = objeto_1
print('{} tem {} anos e {}m de altura'.format(objeto_3.nome, objeto_3.idade, objeto_3.altura))
# Resultado: Ana tem 18 anos e 1.7m de altura

""" pode-se introduzir uma representação em string dentro da própria classe de modo que retorne os 
valores armazenados para um determinado objeto"""

# Utilizando o metodo especial str


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def __str__(self):
        return self.nome+'tem '+str(self.idade)+'anos e '+str(self.altura)+'m de altura'


objeto_1 = Pessoa('Ana', 18, 1.7)
objeto_2 = Pessoa('Joao', 25, 1.8)

print(objeto_1)
print(objeto_2)

# Resultado: Ana tem 18 anos e 1.7m de altura
#            Joao tem 25 anos e 1.8m de altura

"""Pode-se modificar os valores relacionados a um objeto/instância simplesmente atribuindo um novo valor 
ao campo que armazena aquele tipo de dado"""

# Alterando um dado de um objeto


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def __str__(self):
        return self.nome+'tem '+str(self.idade)+'anos e '+str(self.altura)+'m de altura'


objeto_1 = Pessoa('Ana', 18, 1.7)
print(objeto_1)
objeto_1.idade = 19
print(objeto_1)
# Resultado: Ana tem 18 anos e 1.7m de altura
#            Ana tem 19 anos e 1.7m de altura

"""Assim como é possivel criar objetos, o Python permite deletá-los ou deletar alguns de
seus atributos. Realiza-se essa ação por meio do comando 'del'"""

# Deletando atributos e objetos


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def __str__(self):
        return self.nome+'tem '+str(self.idade)+' anos e '+str(self.altura)+'m de altura'


objeto_1 = Pessoa('Ana', 18, 1.7)
print(objeto_1)
del objeto_1.idade
print(objeto_1)
del objeto_1  # aqui apagou-se tudo da classe objeto
print(objeto_1)  # aqui tem erro porque não exixte mais esse objeto uma vez que ele foi deletado
# Resultado: Ana tem 18 anos e 1.7m de altura
#            'Pessoa' object has no attribute '_idade'
#            name 'objeto_1' is not defined

# DEFININDO METODOS DE UMA CLASSE

# Manipulando metodos de uma classe


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def __str__(self):
        return self.nome+'tem '+str(self.idade)+' anos e '+str(self.altura)+'m de altura'

    def ano_nascimento(self, a):
        x = a - self.idade
        return print('{}, voce nasceu em {}'.format(self.nome, x))


ano = int(input('Qual ano em que estamos? '))
pessoa = Pessoa('Ana', 21, 1.8)
pessoa.ano_nascimento(ano)
""""
O método acessa os parâmetros nome, _idade e altura por meio de self. Já o parâmetro ano 
deve ser repassado ao método no momento em que é invocado.
Assim como uma função, um método pode ter parâmetros de entrada ou não e retorno ou não.
"""
# Resultado: Ana, voce nasceu em 2000
#            (isso só ocorre se você colocar que ano = 2021)

# ATRIBUTOS INTRINSECOS
"""
Em Python, toda classe ou objeto possui um conjunto de atributos intrínsecos configurados pelo sistema de execuçao.
As classes possuem os seguintes atributos:
    • __name__: nome da classe;
    • __module__: o módulo ou biblioteca de onde foi carregado;
    • __bases__: coleção de classes básicas;
    • __dict__: um dicionário contendo todos os atributos e métodos da classe;
    • __doc__: a string de documentação.
Para objetos, tem-se os seguintes atributos intrínsecos:
    • __class__: nome da classe do objeto;
    • __dict__: um dicionário contendo todos os atributos do objeto.
"""

# Acesso os atributos intrinsecos de uma classe e objeto
objeto = Pessoa('Ana', 18, 1.7)  # esse obejeto foi colocado para entendermos melhor o cógido
print('Atributos intrinsecos de Classe')
print(Pessoa.__name__)
print(Pessoa.__module__)
print(Pessoa.__doc__)
print(Pessoa.__dict__)
print('Atributos intrinsecos de objeto')
print(objeto.__class__)
print(objeto.__dict__)
"""
Resultado: Atributos intrinsecos de Classe
           Pessoa
           __main__
           None
           {'__module__': '__main__', '__init__': <function Pessoa.
           __init__ at 0x01BEB898>, '__str__': <function Pessoa.__str__ at 0
           x01BEB850>, 'ano_nascimento': <function Pessoa.ano_nascimento at 0
           x01BEB808>, '__dict__': <attribute '__dict__' of 'Pessoa' objects
           >, '__weakref__': <attribute '__weakref__' of 'Pessoa' objects>, '
           __doc__': None}
           
           Atributos intrinsecos de objeto
           <class '__main__.Pessoa'>
           {'nome': 'Ana', '_idade': 18, 'altura': 1.7}
"""

# DADOS E METODOS DE CLASSE

# Explorando variaveis de classe


class Pessoa:
    incremento = 2

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura


objeto = Pessoa('Ana', 18, 1.7)
print(objeto.incremento)
# resultado: 2

# Explorando metodos de classe
"""emprega-se o decorador @classmethod antes de declarar o método,
indicando que o respectivo método relaciona-se com a classe e não com a instância ou
objeto"""


class Pessoa:
    incremento = 0

    def __init__(self, nome, idade, altura):
        Pessoa.incrementar()
        self.nome = nome
        self.idade = idade
        self.altura = altura

    @classmethod
    def incrementar(cls):
        cls.incremento += 1


objeto_1 = Pessoa('Ana', 18, 1.7)
objeto_2 = Pessoa('Joao', 28, 1.7)
# ao ocorrer uma nova formação de um objeto da classe pessoa ocorre o incremento da variável "incremento"
print(Pessoa.incremento)
# Resultado: 2

# METODOS ESTATISTICOS
"""Métodos estáticos constituem um tipo de método que pode ser declarado dentro de
uma classe. Esse método não esta ligado ou a instância/objeto ou a classe, sendo considerados funções independentes."""

# Explorando metodos estaticos


class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    @staticmethod
    def metodo_estatico():
        return 'Metodo estatico'


print(Pessoa.metodo_estatico())
# Resultado: Metodo estatico

# HERANÇA DE CLASSE
"""
Que permite a uma classe herdar os atributos e métodos de uma outra classe.
A classe herdeira é denominada filha ou subclasse, sendo aquela que contêm
os atributos e métodos a classe pai ou classe base.
"""

# Explorando heranca em classes


class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def ano_nascimento(self):
        x = int(input('Em que anos estamos?')) - self.idade
        return print('{}, voce nasceu em {}'.format(self.nome, x))


class dados(Pessoa):

    def __init__(self, nome, idade, altura, cpf):
        super().__init__(nome, idade, altura)
        self.cpf = cpf

    def imprimir(self):
        print('{}, voce tem {} anos, {}m de altura e seu cpf e:{}'.format(self.nome, self.idade, self.altura, self.cpf))


pessoa1 = dados('Ana', 18, 1.7, 121)
pessoa1.imprimir()
# Resultado: Ana, voce tem 18 anos, 1.7m de altura e seu cpf e:121
"""
A classe dados é uma extensão da classe Pessoa. Indica-se essa relação, incluindo o
nome da classe Pessoa entre parênteses após o nome da classe dados. Para que a classe
dados herde os argumentos da classe Pessoa, referencia-se dentro do método especial
__init__ ( ) o construtor da classe Pessoa por meio de super( ).__init__( )
Objetos da classe dados( ) possuem os atributos nome, _idade, altura e cpf e os métodos ano_nascimento( )
e imprimir( ). O método ano_nascimento( ) não está incluso na classe dados. Porém, essa classe o herda por ser
uma extensão da classe Pessoa.
Definese a classe Pessoa como superclasse de dados, pois é a sua classe pai
"""

# SUBSTITUIÇÕES E EXTENSÕES DE METODOS

# Substituicao de metodos


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def informacao(self):
        x = 2021 - self.idade
        return str(self.nome) + ', voce nasceu em ' + str(x)


class dados(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def informacao(self, a):
        x = 2021 - self.idade
        return str(self.nome) + ', voce nasceu em ' + str(x) + ' e sua altura e: ' + str(a)


pessoa1 = Pessoa('Ana', 18)
print(pessoa1.informacao())
pessoa2 = dados('Ana', 18)
print(pessoa2.informacao(1.7))
# Resultado: Ana, voce nasceu em 2003
# Ana, voce nasceu em 2003 e sua altura e: 1.7
"""o método informacao( ) na classe Pessoa e na
classe dados, porém com comandos distintos. Na classe Pessoa, o método informacao( )
retorna uma string que contém o nome e o ano de nascimento de uma pessoa. Em dados,
esse mesmo método retorna uma string com o nome, ano de nascimento e altura de uma
pessoa"""

# Extensao de metodos de superclasse


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def informacao(self):
        x = 2021 - self.idade
        return str(self.nome) + ', voce nasceu em ' + str(x)


class dados(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def informacao(self, a):
        return super().informacao() + ' e sua altura e: ' + str(a)
        # Esse recurso super().'nome do metodo da superclasse' faz com que ela seja transposta
        # do classe pai e seja utilizada


pessoa1 = Pessoa('Ana', 18)
print(pessoa1.informacao())
pessoa2 = dados('Ana', 18)
print(pessoa2.informacao(1.7))
# Resultado: Ana, voce nasceu em 2003
# Ana, voce nasceu em 2003 e sua altura e: 1.7

# MANIPULAÇÃO DE DADOS: METODOS GETTER E SETTER
"""No exemplo a seguir, alterou-se a _idade de uma pessoa por meio do acesso ao atributo _idade do objeto
pessoa"""


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return str(self.nome) + ' tem ' + str(self.idade) + ' anos'


pessoa = Pessoa('Ana', 30)
print(pessoa)
pessoa.idade = 200
print(pessoa)
# Resultado: Ana tem 30 anos
# Ana tem 200 anos

"""
Podem-se implementar métodos específicos para acesso e manipulação de dados por meio do conceito
de encapsulamento. Esses métodos são comumente denotados como setter e getter. 
Os métodos 'setter' permitem acessar um atributo e alterar o valor armazenado, inclusive considerando a
validação dos dados.
Os métodos 'getter' permitem acessar o valor armazenado por um determinado atributo.
"""

"""Para o exemplo anterior, introduzem esses métodos para os
atributos nome e _idade. Note que a tentativa de alterar a _idade da pessoa falhou pois não
se enquadra nas condições estabelecidas para o método set_idade( )"""
# Explorando metodos setter e getter


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return str(self.nome) + ' tem ' + str(self.idade) + ' anos'

    def get_nome(self):
        return self.nome

    def set_idade(self, nova_idade):
        if (0 <= nova_idade <= 100) and isinstance(nova_idade, int):
            self.idade = nova_idade

    def get_idade(self):
        return self.idade


pessoa = Pessoa('Ana', 30)
print(pessoa)
pessoa.set_idade(200)
print(pessoa)
# Resultado: Ana tem 30 anos
#            Ana tem 30 anos

"""
Para tornar a manipulação de métodos setter e getter mais intuitiva, introduziu-se
no Python 2.2 um conceito denominado de propriedade. Isso possibilitou a introdução
de comandos que atrelam esses métodos a uma determinada propriedade
Onde fget indica o método getter, fset indica o método setter, fdet indica um método
para deletar dados e doc provê a documentação da propriedade. Esses parâmetros são
opcionais.
"""

# Explorando metodos setter e getter com propriedades


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return str(self.nome) + ' tem ' + str(self.idade) + ' anos'

    def get_nome(self):
        return self.nome

    n = property(get_nome)

    def set_idade(self, nova_idade):
        if (0 <= nova_idade <= 100) and isinstance(nova_idade, int):
            self.idade = nova_idade

    def get_idade(self):
        return self.idade

    i = property(get_idade, set_idade)


pessoa = Pessoa('Ana', 30)
print(pessoa)
pessoa.i = 200
print(pessoa)
"""nota-se uma simplificação na notação do método setter. """
# Resultado: Ana tem 30 anos
#            Ana tem 30 anos

# acesso de dados do codigo anterior
pessoa = Pessoa('Ana', 30)
print(pessoa.n)
print(pessoa.i)
# Resultado: Ana
#            30

"""
Para simplificar a declaração de Propriedades, a versão Python 2.4 introduziu os decoradores @property, 
@<nome_propriedade>.setter e @<nome_propriedade>.deleter.
Aplicam-se esses decoradores no exemplo anterior e elimina-se a linha de comando para declaração da Propriedade
Uma alteração importante é que os métodos setter e getter de um determinado atributo
passam a ter os mesmos nomes, sendo que os decoradores distinguem as suas funções
"""
# Explorando metodos setter e getter


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return str(self.nome) + ' tem ' + str(self.idade) + ' anos'

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


pessoa = Pessoa('Ana', 30)
pessoa.i = 200
print(pessoa.n)
print(pessoa.i)
pessoa.i = 200
# Resultado: Ana
#            30

# MODULO
"""
Módulos e pacotes são estruturas utilizadas pela linguagem Python para organizar e
modularizar programas extensos.
Módulos permitem agrupar estruturas como classes, funções e até mesmo linhas de código gerais.
Em Python, considera-se um módulo um arquivo .py que contém códigos em Python
como funções, classes, códigos executáveis e atributos relacionados ao módulo. 
O nome de um módulo corresponde ao nome do arquivo .py que contêm os comandos
"""

"""Após importar o módulo, tem-se acesso as suas funções, classes e variáveis"""


import exmodulo


person = exmodulo.Person('John', 54)
print(person)
# Resultado: Ola, esse modulo possui uma classe Person
# John tem 54 anos de idade

""" Por exemplo, importa-se o módulo ‘exmodulo’ como ‘m’ empregando a palavra-chave 'as'"""


import exmodulo as m


person = m.Person('John', 54)
print(person)
# Resultado: Ola, esse modulo possui uma classe Person
#            John tem 54 anos de idade

"""Na manipulação de módulos, pode-se importar apenas uma função ou classe desse
módulo. Considere que o módulo ‘exmodulo’ tenha agora uma função que retorna uma
mensagem qualquer. """

from exmodulo import mensagem


mensagem()
# Resultado: Ola, esse modulo possui uma classe Person
# Ola, sou uma funcao do modulo exmodulo

"""Note o uso da palavra-chave ‘from’ e a sintaxe para importar estruturas específicas.
No exemplo anterior, a função mensagem( ) pode ser renomeado utilizando palavra-chave
as como ‘novafuncao"""

from exmodulo import mensagem as novafuncao


novafuncao()
# Resultado: Ola, esse modulo possui uma classe Person
#            Ola, sou uma funcao do modulo exmodulo

"""os módulos possuem propriedades relacionadas ao nome(__nome__),
docstring (__doc__) e nome do arquivo (__file__). Obtém-se o conteúdo do módulo por
meio do comando dir(<module-name>)"""

# CLASSES BASES ABSTRATAS

"""
As ABC’s classes que não podem ser instanciadas (criar um objeto) e que têm o propósito
de se estender para uma ou mais subclasses por meio de herança. 
Nessas subclasses, os métodos podem ser reescritos de acordo com a finalidade da classe.
Pode-se ter um método calcula_salario( ) que é comum a um conjunto de classes, que calcula o salário de diferentes
funcionários de uma empresa.
Em Python, define-se uma classe abstrata especificando que a classe tem uma metaclasse, tipicamente, ABCMeta. 
Essa metaclasse é oriunda do módulo abc. Especifica-se a metaclasse por meio de seu atributo na lista de classes pai.
"""

from abc import ABCMeta, abstractmethod


class Salario(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calcula_salario(self):
        pass

class Chefe(Salario):

    def __init__(self, horas, bonus):
        self._horas = horas
        self._bonus = bonus

    def calcula_salario(self):
        x = 200 * self._horas + self._bonus
        return print ('Salario (Chefe):', x)

class Secretaria(Salario):

    def __init__(self, horas):
        self._horas = horas

    def calcula_salario(self):
        x = 100* self._horas
        return print ('Salario (Secretaria):', x)


funcionario = Chefe(160, 13000)
funcionario.calcula_salario()
funcionario = Secretaria(160)
funcionario.calcula_salario()
# Resultado: Salario (Chefe): 45000
#            Salario (Secretaria): 16000

# SUBCLASSE VIRTUAL
"""No exemplo abaixo, declara-se uma classe ABC e, em seguida, uma segunda classe
que é registrada como classe virtual da primeira"""

from abc import ABCMeta, abstractmethod


class Salario(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calcula_salario(self):
        pass


class Chefe:

    def __init__(self, horas, bonus):
        self._horas = horas
        self._bonus = bonus

    def calcula_salario(self):
        x = 200 * self._horas + self._bonus
        return print ('Salario (Chefe):', x)


Salario.register(Chefe)
print(issubclass(Chefe, Salario))
#Resultado: True

# MIXINS
"""Uma classe mixins representa funcionalidades que podem ser empregadas em múltiplas situações. Porém, individualmente
não possui aplicação direta. Pode-se mixar esse tipo de classe em outras classes, estendendo suas funcionalidades"""

from abc import ABCMeta, abstractmethod


class Imprimir(metaclass=ABCMeta):

    def printar(self):
        print(self)


class Salario(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calcula_salario(self):
        pass


class Chefe(Salario, Imprimir):

    def __init__(self, horas, bonus):
        self._horas = horas
        self._bonus = bonus

    def calcula_salario(self):
        x = 200 * self._horas + self._bonus
        return print ('Salario (Chefe):', x)

    def __str__(self):
        return 'Chefe trabalhou: ' + str(self._horas) + ' e teve um bonus de ' + str(self._bonus)


funcionario = Chefe(160, 13000)
funcionario.printar()
# Resultado: Chefe trabalhou: 160 e teve um bonus de 13000
