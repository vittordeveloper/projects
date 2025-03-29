# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0
ano = date.today().year

for i in range(0, 3):
    idade = int(input(f'Em que ano a {i + 1}º pessoa nasceu: '))
    atual = ano - idade
    if atual > 18:
        maior += 1
    else:
        menor += 1

print(f'Ao todo tem {maior} pessoas maior de idade')
print(f'Ao todo tem {menor} pessoas menor de idade')