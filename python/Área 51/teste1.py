import time as t

# Tempo de carregamento total
tempo_total = 5
tempo_passado = 0

while tempo_passado < tempo_total:
    print('\r.  ', end='')
    t.sleep(0.5)
    tempo_passado += 0.5
    print('\r.. ', end='')
    t.sleep(0.5)
    tempo_passado += 0.5
    print('\r...', end='')
    t.sleep(0.5)
    tempo_passado += 0.5

print('\rCarregou!')
