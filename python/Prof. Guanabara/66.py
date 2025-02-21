# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = 0

while True:
    entrada = input('Digite um número (ou a palavra PARE para somar eles): ')

    if entrada.upper() == 'PARE':
        break

    n1 = int(entrada)
    soma += n1
print(soma)