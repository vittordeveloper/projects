# Crie uma classe Livro com propriedades titulo, autor e anoPublicacao. Adicione um método para exibir as informações do livro e crie instâncias para testar a classe.

class Livro:
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano = anoPublicacao

Livro1 = Livro('Fim Do Mundo', 'Rebeca de Londrino', '2007')
Livro2 = Livro('Romeu e Julieta', 'Theodoro Benfica', '2003')

Livro1.titulo, Livro1.autor, Livro1.ano

print('='*30)
for i, chave in vars(Livro1).items():
    print(f'{i}: {chave}')

print('='*30)
for i, chave in vars(Livro2).items():
    print(f'{i}: {chave}')

print('='*30)