#classe = molde
class Usuario:

    #variavel da classe
    nome_variavel_exemplo = 1234

#método = função da classe
#def: método = precisa da instancia do def__init__
    def __init__(self):
        pass
    def exemplo(self):
        pass

#@classmethod = só precisa do valor da classe
    @classmethod
    def exemplo_method2(cls):
        pass

#@staticmethod = não precisa de nenhum dos dois (instância ou valor da classe)
    @staticmethod 
    def exemplo_method3():
        pass

#getter e setter = proteção/filtro dos atributos
#getter = obter um valor antes de passar para a classe
    @property 
    def nome_variavel(self):
        return self._nome_variavel

#setter = informar o valor à classe'''
    @nome_variavel.setter
    def nome_variavel(self):
        #o que vai mudar
        novo_nome_variavel: None
        self._nome_variavel = novo_nome_variavel

#instância
#nome da instancia = classe que ela faz parte()
usuario = Usuario()

#alterar valor da variavel da classe
#nome da classe.nome da variavel da classe = 'novo valor'
Usuario.nome_variavel_exemplo = 4321