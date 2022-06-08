#função update() -> atualiza a lista com elementos de outro objeto
#função super() -> invoca um metodo ou parametro da classe pai

#classe -> molde
class Usuario:

    #variavel da classe
    nome_variavel_exemplo = 1234

#método -> função da classe
    #def: método -> precisa da instancia
    #__init__ -> construtor // o mais próximo que existe de um construtor
    def __init__(self):
        self.exemplo_variavel = {}

#exemplo de método
    def nome_do_método(self):
        pass

#@classmethod -> só precisa da variavel da classe
    @classmethod
    def exemplo_method2(cls):
        pass

#@staticmethod -> não precisa de nenhum dos dois (instância ou variavel da classe)
    @staticmethod 
    def exemplo_method3():
        pass

#getter e setter -> proteção/filtro dos atributos
    #getter -> obter um valor antes de passar para a classe
    #@property -> obtem esse valor para acessar fora da classe
    @property 
    def nome_variavel(self):
        return self._nome_variavel

#setter -> informar o valor à classe
#@nome_variavel.setter precisa do @property antes
    @nome_variavel.setter
    def nome_variavel(self):
        #o que vai mudar
        novo_nome_variavel: None
        self._nome_variavel = novo_nome_variavel

#encapsulamento -> esconder partes do código para proteger classe/método
    #public, protected, private
        
        #público: acessivel dentro e fora da classe
        
        #protegido: acessivel apenas dentro da classe ou das filhas da classe
            #self._nome da variavel
        
        #privado: só está disponível dentro da classe
            #self.__nome da variavel 

#instância
    #nome da instancia -> classe que ela faz parte()
usuario = Usuario()
#alterar valor da variavel da classe
    #nome da classe.nome da variavel da classe -> 'novo valor'
Usuario.nome_variavel_exemplo = 4321

'''***********************************************************'''

#associação -> uma classe se relaciona com outra classe mas são independentes
    #usa

class Nome01:
    def __init__(self, valor01):
        self.__valor01 = None
    #getter
    @property
    def valor01(self):
        return self.__valor01
    
    @valor01.setter
    def valor01(self, valor01):
        self.__valor01 = valor01

    def acao01(self):
        print('acao01')

class Nome02:
    def acao02(self):
        print('acao02')

variavel01 = Nome01('valor01')
variavel02 = Nome02()

#associacao da classe Nome01 e Nome02
variavel01.valor01 = variavel02
#a classe Nome01 executou um método da classe Nome02
variavel01.valor01.acao02()

print('*'*30)
'''***********************************************************'''

    #agregação -> uma classe usa outra classe e precisa da outra classe
        #tem

class nome_classe_01:
    def __init__(self):
        self.nome01 = []
    #adiciona item na lista
    def acao01(self,nome_classe_02):
        self.nome01.append(nome_classe_02)
    #mostrando a lista
    def acao02(self):
        for nome_classe_02 in self.nome01:
            print(nome_classe_02.nome03, nome_classe_02.nome04)
    #somando o valor que tem na lista
    def acao03(self):
        nome02 = 0
        for nome_classe_02 in self.nome01:
            nome02 += nome_classe_02.nome04
        return nome02

class nome_classe_02:
    def __init__(self, nome03, nome04):
        self.nome03 = nome03
        self.nome04 = nome04
    
variavel_nome01 = nome_classe_01()

variavel_nome02 = nome_classe_02('item01', 1)
variavel_nome03 = nome_classe_02('item02', 2)
variavel_nome04 = nome_classe_02('item03', 3)

variavel_nome01.acao01(variavel_nome02)
variavel_nome01.acao01(variavel_nome03)
variavel_nome01.acao01(variavel_nome04)
variavel_nome01.acao02()
print(variavel_nome01.acao03())

print('*'*30)
'''***********************************************************'''

    #composição -> uma classe vai ser dona de objetos de outra classe
    #se for apagada as outras classes também serão apagadas
        #é dono

class Name01:
    def __init__(self, value01, value02):
        self.value01 = value01
        self.value02 = value02
        self.value03 = []
    #insere os valores da classe Nome02 na lista value03
    def insert_value03(self, value04, value05):
        self.value03.append(Name02(value04, value05))
    #listar os valores do value03
    def print_value03(self):
        for Name02 in self.value03:
            print(Name02.value04, Name02.value05)

class Name02:
    def __init__(self, value04, value05):
        self.value04 = value04
        self.value05 = value05

user01 = Name01('name01', 1)
user01.insert_value03('text01', 'text02')
print(user01.value01)
user01.print_value03()

user02 = Name01('name02', 2)
user02.insert_value03('text03', 'text04')
print(user02.value01)
user02.print_value03()

user03 = Name01('name03', 3)
user03.insert_value03('text06', 'text07')
print(user03.value01)
user03.print_value03()

print('*'*30)
'''***********************************************************'''

#herança -> a nova classe herda os atributos e comportamentos dessa classe existente
    #é

    #superclasse:
class Test01:
    def __init__(self, value01, value02):
        self.value01 = value01
        self.value02 = value02
        self.nameclass = self.__class__.__name__
    #este método pertence somente a todas à superclasse e as subclasses/herdeiras/filhas
    def acao01(self):
        print(f'{self.nameclass} fazendo açao01')

#a classe Test02 está herdando tudo da classe Test01
    #subclasse
class Test02(Test01):
    #este método pertence somente à esta classe
    def acao02(self):
        print(f'{self.nameclass} fazendo açao02')

class Test03(Test01):
    #este método pertence somente à esta classe
    def acao03(self):
        print(f'{self.nameclass} fazendo açao03')

variable01 = Test01('value01', 1)
print(variable01.value01)
variable01.acao01()

variable02 = Test02('value02', 2)
print(variable02.value01)
variable02.acao01()
variable02.acao02()

variable03 = Test03('value03', 3)
print(variable03.value01)
variable03.acao01()
variable03.acao03()