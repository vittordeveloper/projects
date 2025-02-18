# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = (
    'Arroz', 2.90, 'Paqueca', 3.40, 'Arroz', 5.40)

for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end='')
    else:
        print(f'R${produtos[i]:>5.2f}')