# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

import random as r
print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*20)

while True:
    escolha = ' '
    while escolha not in 'PI':
        escolha = (input('Escolha (P)ar ou (I)impar: ')).upper()[0]
    valor = int(input('Digite um número: '))
    pc = r.randint(1, 10)
    soma = valor + pc
    print(f'Você digitou o número {valor} e a máquina o número {pc} que deu {soma}')

    if escolha == 'P':
        if soma % 2 == 0:
            print('VOCÊ GANHOU')
        else:
            print('A máquina ganhou!')
    if escolha == 'I':
        if soma % 2 == 1:
            print('VOCÊ GANHOU')
        else:
            print('A máquina ganhou!')
    novo = input('Quer jogar denovo? s/n: ').upper()
    if novo == 'S':
        continue
    else:
        print('Programa encerrado!') 
        break