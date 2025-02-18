# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n1 = int(input('Digite um número: '))

for i in range (1, 10+1):
    print(f'{n1} x {i} = {n1 * i}')