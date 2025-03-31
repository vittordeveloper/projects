# Crie uma classe Carro com propriedades modelo e ano. Adicione um método para exibir os dados do carro e instancie dois objetos dessa classe no main.

class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def ExibirInfos(self):
        print(self.modelo, self.ano)

Carro1 = Carro('HB20', '2012')

Carro1.ExibirInfos()