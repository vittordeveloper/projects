# Crie uma função que receba uma lista de números e retorne o maior valor encontrado. Se a lista estiver vazia, retorne 0.

lista = [1, 2]

def maior_menor(a):
    if not a:
        print('Não contém números')
        return
    
    print(f'O maior dessa lista é o {max(a)} e o menor é o {min(a)}')

maior_menor(lista)