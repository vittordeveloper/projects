# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Digite a velocidade em que se anda o carro: '))


if velocidade > 80:
    soma = 7 * (velocidade - 80)
    print(f'Você foi multado em R${soma}')
else:
    print('Tenha um bom dia! Dirija com segurança')