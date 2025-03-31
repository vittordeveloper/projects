# Crie um programa que defina uma constante para a taxa de câmbio (por exemplo, 5.0) e converta um valor em dólares para reais, exibindo o resultado

taxa = 5.6755
dolar = int(input('Digite um valor para ser convertido em REAIS: ')) # Dei uma aprimorada
reais = dolar * taxa

print(f'{dolar} dolares são {reais:.2f} reais')