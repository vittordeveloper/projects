def robux(quantidade, preco, cupom_de_desconto=''):

    if cupom_de_desconto == 'AKATSUKI':
        return preco * quantidade * 0.9
    else:
        return preco * quantidade

print('Preço dos robux: R$30.00 = 1000')

while True:
    cupom = input('Deseja adicionar algum cupom de desconto? ("N" para prosseguir): ').upper()
    if cupom == 'N':
        break
    if cupom == 'AKATSUKI':
        break
    else:
        print('Cupom Inválido')
        continue


while True:
    try:
        quantidade = int(input('Quantos robux você deseja?: '))
    except ValueError:
        print('Não consegui entender, pode digitar novamente?')
        continue
    continuar = input(f'Você deseja {quantidade} Robux, isso dá: R${robux(quantidade, preco=0.03, cupom_de_desconto=cupom)} confere? (s/n): ').upper()
    if continuar == 'S':
        break
    else:
        continue


print(f'Pague no PIX o valor de: R${robux(quantidade, preco=0.9, cupom_de_desconto=cupom)}')