# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('Diga uma frase qualquer: ').strip().upper()
palavras = frase.split()
lista = ''.join(palavras)
inverso = ''

for c in range(len(lista) - 1, -1, -1):
    inverso += lista[c]
if inverso == lista:
    print('é uma palavra palíndromo')
else:
    print('N é palíndromo')