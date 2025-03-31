# Crie um programa que utilize um loop while para simular um jogo de adivinhação: o programa deve continuar pedindo um número até que o usuário adivinhe o número correto (defina o número fixo no código).

while True:
    n1 = int(input('Digite um número: '))
    if n1 == 6:
        break

print('Você acertou!')