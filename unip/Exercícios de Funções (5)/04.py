# Crie uma função com parâmetros nomeados que receba o nome e a idade de uma pessoa e retorne uma mensagem formatada. Exiba o resultado no main.

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

def boas_vindas(a, b):
    print(f'Boas vindas {nome}, você tem {idade} anos certo?')

if __name__ == '__main__':
    boas_vindas(nome, idade)