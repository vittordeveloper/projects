# Crie um programa que peça para o usuário digitar números até que o número zero seja digitado. Ao final, exiba a soma dos números informados.

nums = []

while True:
    n1 = int(input('Digite um número: '))
    if n1 == 0:
        break
    else:
        nums.append(n1)

novo = sum(nums)

print(novo)