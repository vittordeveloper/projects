# Faça uma função que retorne uma lista ordenada, exemplo 85554, retorna: [8, 5, 5, 5, 4]

num1 = int(input('Digite um número: '))

def ordenada(num1):
    num_str = str(num1)
    lista_ordenada = [int(digito) for digito in num_str]
    lista_ordenada.sort()
    return lista_ordenada

print(ordenada(num1))