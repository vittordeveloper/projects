# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times.b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

times_brasileirao = (
    "Botafogo", "Palmeiras", "Fortaleza", "Flamengo", "São Paulo", 
    "Internacional", "Bahia", "Cruzeiro", "Atlético-MG", "Vasco da Gama", 
    "Fluminense", "Criciúma", "Grêmio", "Red Bull Bragantino", "Juventude", 
    "Vitória", "Corinthians", "Athletico-PR", "Cuiabá", "Atlético-GO"
)

print(
    '[1] 5 primeiros times\n'
    '[2] Os últimos 4 colocados\n'
    '[3] Times em ordem alfabética\n'
    '[4] Em que posição está o time da Juventude.\n'
)

escolha = int(input('Digite um número: '))
if escolha == 1:
    for index, time in enumerate(times_brasileirao[:5]): print(f'{index + 1}. {time}')
elif escolha == 2:
    print(times_brasileirao[-4:])
elif escolha == 3:
    for index, times in enumerate(sorted(times_brasileirao)): print(f'{index + 1}. {times}')
elif escolha == 4:
    print(f'O Juventude está na posição {times_brasileirao.index('Juventude')+164}')