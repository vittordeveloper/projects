# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    n1 = int(input('Quer ver a tabuada de que número?: '))
    if n1 > 0:
        for c in range(1, 10+1):
            print(f'{n1} x {c} = {c * n1}')
    else:
        print('Programa encerrado, volte mais tarde')
        break