class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def exibir(self):
        print('Nome: ', self.nome, '\nSobrenome: ', self.sobrenome, '\nIdade: ', self.idade)

class Empregado(Pessoa):
    def __init__(self, matricula: int): 
        self.matricula = matricula

class Chefe(Pessoa):
    def __init__(self, matricula: int): 
        self.matricula = matricula

p1 = Pessoa('nome', 'sobrenome', 16)
p1 = Chefe(1)
print(p1.exibir, p1.matricula)