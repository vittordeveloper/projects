# Crie uma classe Pessoa com propriedades nome e idade. Adicione um método para exibir as informações da pessoa e instancie um objeto dessa classe no main.

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ExibirInfoDasPessoas(self):
        print(self.nome, self.idade)    

Pessoa1 = pessoa('Brenno', '18')

if __name__ == '__main__':
    Pessoa1.ExibirInfoDasPessoas()