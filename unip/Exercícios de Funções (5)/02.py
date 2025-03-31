# Crie uma função que receba uma string e retorne a mesma string invertida. Exiba o resultado no main.

def inverso(palavra):
    novo = palavra[::-1]
    return novo

if __name__ == '__main__':
    print(inverso('Abacadraba'))