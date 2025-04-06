from cadastro import *
from time import sleep

# Caso o arquivo dados.txt não estiver funcionando, apague ele e depois deixe com que a própria máquina crie.
# Menu principal
while True:
    menu_principal('MENU PRINCIPAL')
    exibir_opcoes(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema', 'Limpar dados'])

    try:
        escolha = opcoes()

        if escolha == 3:
            print('Saiu com Sucesso!')
            break

        elif escolha == 2:
            nova_pessoa('CADASTRAR NOVA PESSOA')
            try:
                nome = input('Digite o nome da pessoa: ')
                idade = int(input('Digite a idade: '))
                cidade = input('Digite a cidade: ')

                with open('dados.txt', 'a', encoding='utf-8') as arquivo:
                    arquivo.write(f'NOME: {nome}\nIDADE: {idade}\nCIDADE: {cidade}\n')
                    print('Registrando...')
                    sleep(3)
            except Exception as e:
                print(f'Erro ao cadastrar: {e}')
        
        elif escolha == 1:
            try:
                with open('dados.txt', 'r', encoding='utf-8') as leitura:
                    print('Puxando dados...')
                    sleep(1.5)
                    print(42*'-')
                    print('PESSOAS CADASTRADAS'.center(42))
                    print(42*'-')
                    print(leitura.read())
                    sleep(2)
            except FileNotFoundError:
                print('Erro, o arquivo não existe, você precisa registrar alguém!')
                sleep(3)

        elif escolha == 4:
            while True:
                try:
                    pergunta_usuario = input('Deseja mesmo apagar? (S/N): ').upper().strip()[0]
                    if pergunta_usuario == 'S':
                        with open('dados.txt', 'w', encoding='utf-8') as limpar:
                            pass
                        print('Limpando fichário')
                        sleep(1.5)
                        print('Ficha limpa com sucesso')
                        break
                    elif pergunta_usuario == 'N':
                        break
                    else:
                        print('Opção Inválida, por favor digite novamente!')
                except Exception as e:
                    print(f'Ocorreu um erro ao limpar os dados: {e}')

    except ValueError:
        print('Entrada inválida! Digite apenas números nas opções do menu.')
