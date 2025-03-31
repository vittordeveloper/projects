# Crie uma classe Animal com propriedades nome e idade. Adicione um método que retorne o som do animal (você pode definir um valor fixo, como "Au Au" ou "Miau") e instancie um objeto para exibir o resultado.


class Animal:
    def __init__(self, nome, idade, som):
        self.nome = nome
        self.idade = idade
        self.som = som

    def SomDoAnimal(self):
        print(self.som)

Cachorro = Animal('Toby', '7 Anos', 'Au Au')
Gato = Animal('Tom', 'Falecido/Sumido', 'Miau')

Cachorro.SomDoAnimal()
Gato.SomDoAnimal()