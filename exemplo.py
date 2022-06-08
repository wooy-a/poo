class Pessoa: #Classe base; pai; superclasse
    def __init__(self, nome: str, sobrenome: str, idade: int):
        #self.nome = variavel // nome = parametro
        self.nome = nome 
        self.sobrenome = sobrenome
        self.idade = idade

    def infoP(self):
        print('Nome: ', self.nome, '\nSobrenome: ', self.sobrenome, '\nIdade: ', self.idade)

class Empregado(Pessoa): #Filho; subclasse
    #deve ser passado os parametros da classe pai que serão usados na classe filho
    def __init__(self, nome, sobrenome, idade: int, matricula: int): 
        self.matricula = matricula
        
            #super() está invocando parametro
        super().__init__(nome, sobrenome, idade)

    def infoE(self):
        print('Empregado\n')
            #super() está invocando metodo
        super().infoP()
        print('Matrícula: ', self.matricula)

class Chefe(Pessoa): #Filho; subclasse
    def __init__(self, nome, sobrenome, idade: int, matricula: int): 
        self.matricula = matricula
        super().__init__(nome, sobrenome, idade)

    def infoC(self):
        print('Chefe\n')
        super().infoP()
        print('Matrícula: ', self.matricula)

print('-'*30)
p1 = Chefe('Maria', 'Silva', 23, 1)
p1.infoC()
print('-'*30)
p2 = Empregado('João', 'Santos', 28, 1365)
p2.infoE()
print('-'*30)