#  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
n = ' '.join(map(str, numeros))
print(f'Eu sorteei os seguintes números:', n)
print(f'o maior número é o:', max(numeros))

print(f'o menor número é o:', min(numeros))