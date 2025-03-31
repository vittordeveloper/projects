# Crie um programa que receba um valor numérico e, utilizando if-else, classifique-o como negativo, zero ou positivo

n1 = int(input('Digite um número: '))

if (n1 <= -1):
    print('O número é negativo')
elif (n1 == 0):
    print('É um zero')
else:
    print('O número é positivo')