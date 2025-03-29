# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista = []
for i in range(2):
    peso = float(input(f'Diga o peso da {i + 1}º pessoa: '))
    lista += [peso]

print(f'A pessoa mais pesada da lista é a: {max(lista)}')
print(f'A pessoa mais leve da lista é a: {min(lista)}')