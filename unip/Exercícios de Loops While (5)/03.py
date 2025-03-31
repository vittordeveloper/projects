# Crie um programa que utilize um loop while para contar quantas vezes um número negativo foi digitado (você pode simular a entrada de números com uma lista)

lista = []

while True:
    n1 = int(input('Digite 0 para parar: '))
    if n1 == 0 or n1 > 0:
        break
    else:
        lista.append(n1)

print(f'Você digitou {len(lista)} números negativos')
