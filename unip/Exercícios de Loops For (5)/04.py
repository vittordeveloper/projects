# Crie um programa que exiba a tabuada de um número (por exemplo, a tabuada de 5) utilizando um loop for.

n1 = int(input('Digite um número: '))

for i in range(1, 10+1):
    print(f'{n1} x {i} = {n1*i}')