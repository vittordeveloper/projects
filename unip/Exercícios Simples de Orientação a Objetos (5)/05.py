# Crie uma classe Produto com propriedades nome, preco e quantidade. Crie um método para calcular o valor total do produto (preço * quantidade) e exiba o resultado no main.

class Produto():
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

    def calcular(self):
        print(self.preço * self.quantidade)

Produto1 = Produto('Arroz', 12.99, 2)
Produto2 = Produto('Feijão', 19.99, 1)

if __name__ == '__main__':
    Produto2.calcular()