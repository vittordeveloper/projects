# criar uma array que retorne o alfabeto, exemplo 1 e 2 --# Saida: ['A', 'B']

tupla = (
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
)



users = int(input('Digite um número: '))

if users <= 26:
    print(', '.join(tupla[:users]))
else:
    print('Número passou do limite, existem apenas 26 letras no Alfabeto')
if users < 0:
    print('Não existe letra negativa')