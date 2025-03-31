# Crie um programa que receba a idade de uma pessoa e determine se ela é maior de idade ou não. Exiba uma mensagem apropriada.

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')