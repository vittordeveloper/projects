# Criando tuplas
tupla_vazia = ()               # Tupla vazia
tupla_uma_palavra = ("Python",) # Tupla com um elemento (vírgula é necessária)
tupla_varios = (1, 2, 3, "Olá", 4.5) # Tupla com diferentes tipos de dados

# Acessando elementos
print(tupla_varios[0]) # Saída: 1
print(tupla_varios[-1]) # Saída: 4.5

# Fatiamento
print(tupla_varios[1:4]) # Saída: (2, 3, 'Olá')

# Verificando o tamanho
print(len(tupla_varios)) # Saída: 5
