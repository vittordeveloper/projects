# Utilizando o operador ternário, crie um programa que compare dois números e exiba o maior deles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

maior = n1 if n1 > n2 else n2


print(f'O maior é o {maior}')