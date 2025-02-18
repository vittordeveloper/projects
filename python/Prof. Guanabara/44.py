'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros'''

while True:
    carrinho = float(input('Digite o total em R$: '))
    print(
        '[1] à vista dinheiro/cheque: 10% de desconto\n'
        '[2] à vista no cartão: 5% de desconto\n'
        '[3] em até 2x no cartão: preço formal\n'
        '[4] 3x ou mais no cartão: 20% de juros'
    )
    desejo = int(input('Como deseja PAGAR?'))


    if desejo == 1:
        preco = carrinho - (carrinho * 10 / 100)
        print(f'O total de {carrinho:.0f} com 10% de desconto saíra por R${preco}')
    elif desejo == 2:
        preco = carrinho  - (carrinho * 5 / 100)
        print(f'O total de {carrinho:.0f} com 5% de desconto saíra por R${preco}')
    elif desejo == 3:
        preco = carrinho / 2 
        print(f'O total de {carrinho:.0f} saíra por: 2x PARCELAS de R${preco}')
    elif desejo == 4:
        quantidade = int(input('Qual o Número de PARCELAS?: '))
        preco = carrinho + (carrinho * 20 / 100)
        parcelas = carrinho / quantidade
        print(f'O total de {carrinho} saíra por: {quantidade} PARCELAS de R${parcelas}')
    
    else:
        print('Comando errado, tente novamente')