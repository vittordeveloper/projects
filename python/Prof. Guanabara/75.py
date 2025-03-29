'''   Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

n1 = (
    int(input('Digite um valor: ')),
    int(input('Digite outro Valor: ')),
    int(input('Digite mais um: ')),
    int(input('Digite mais um: '))
)

if 9 in n1:
    print(f'Apareceu o número 9: {n1.count(9)} vezes')
else:
    print('Não foi encontrado nenhum 9')

if 3 in n1:
    print(f'O valor 3  foi encontrado na {n1.index(3)+1} posição')
else:
    print('Nenhum 3 foi encontrado')

for c in n1:
    if c % 2 == 0:
        print(f'Numeros pares encontrados: {c}')
