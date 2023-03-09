from abc import ABCMeta, abstractmethod  # modulo que 'chama' a classe abstrata


# Classe abstrata que define o salario
class Salario(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calcula_salario(self):
        pass


# Classe do grupo 1, este que possui bonus
class Grupo_1(Salario):

    def __init__(self, horas):
        self._horas = horas
        self.salario = 0

    def calcula_salario(self):
        self.salario = 200 * self._horas
        self.salario = self.salario * 1.3
        return print('Salario de R$', self.salario)


# Classe do grupo 2, este que não possui bonus
class Grupo_2(Salario):

    def __init__(self, horas):
        self._horas = horas
        self.salario = 0

    def calcula_salario(self):
        self.salario = 250 * self._horas
        return print('Salario de R$', self.salario)


# Quantidade de pessoas que estão no grupo 1 (que tem bonus)
y = int(input('Quantidade de pessoas que são do Grupo 1 (que tem bonus): '))
for i in range(y):
    x = float(input('Horas trabalhadas pelo trabalhador {} do grupo 1: '.format(i+1)))
    funcionario = Grupo_1(x)
    funcionario.calcula_salario()

# Quantidade de pessoas que estão no grupo 2 (que não tem bonus)
y = int(input('Quantidade de pessoas que são do Grupo 1 (que tem bonus): '))
for i in range(y):
    x = float(input('Horas trabalhadas pelo trabalhador {} do grupo 2: '.format(i+1)))
    funcionario = Grupo_2(x)
    funcionario.calcula_salario()
"""
RESULTADO:
    Quantidade de pessoas que são do Grupo 1 (que tem bonus): 2
    Horas trabalhadas pelo trabalhador 1 do grupo 1: 10
    Salario de R$2600.0
    Horas trabalhadas pelo trabalhador 2 do grupo 1: 25
    Salario de R$6500.0
    Quantidade de pessoas que são do Grupo 1 (que tem bonus): 3
    Horas trabalhadas pelo trabalhador 1 do grupo 2: 16
    Salario de R$4000.0
    Horas trabalhadas pelo trabalhador 2 do grupo 2: 40
    Salario de R$10000.0
    Horas trabalhadas pelo trabalhador 3 do grupo 2: 23
    Salario de R$5750.0
"""
