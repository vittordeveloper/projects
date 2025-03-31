# Crie um programa que receba uma nota de 0 a 100 e exiba o conceito (A, B, C, D ou E) de acordo com a seguinte escala:

nota = int(input("Digite a nota (0-100): "))

if nota >= 90:
    conceito = "A"
elif nota >= 80:
    conceito = "B"
elif nota >= 70:
    conceito = "C"
elif nota >= 60:
    conceito = "D"
else:
    conceito = "E"

print(f"O conceito da nota {nota} é: {conceito}")
