def menu_principal(msg):
    print(42*'-')
    print(msg.center(42))
    print(42*'-')

def exibir_opcoes(opcao):
    for index, opcoes in enumerate(opcao):
        print(index + 1, opcoes)

def opcoes():
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        return 1
    elif opcao == 2:
        return 2
    elif opcao == 3:
        return 3
    elif opcao == 4:
        return 4
    
def nova_pessoa(msg):
    print(42*'-')
    print(msg.center(42))
    print(42*'-')