# Transforme um relógico dada sua base em Horas, Minutos e segundos e converta o para segundos

relogio = str(input('Que horas são: '))

def segundo(relogio):
    horas, minutos, segundos = map(int, relogio.split(':'))

    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

print(segundo(relogio))