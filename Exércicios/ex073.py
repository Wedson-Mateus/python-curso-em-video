times = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Bragantino', 'Corinthians', 'Fortaleza', 'Internacional',
         'Fluminense', 'América-MG', 'Ceara-SC', 'Athletico-PR', 'Santos', 'Cuiabá', 'Atlético-GO', 'São Paulo',
         'Bahia', 'Juventude', 'Sport Recife', 'Grêmio', 'Chapecoense')
print('-=-' * 20)
print(f'Lista dos times do Brasileirão:\n{times}')
print('-=-' * 20)
print(f'Os 5 primeiros são:\n{times[0:5]}')
print('-=-' * 20)
print(f'Os 4 últimos são:\n{times[-4:]}')
print('-=-' * 20)
print(f'Os times em ordem alfabética:\n{sorted(times)}')
print('-=-' * 20)
print(f'O Chapecoense está em {times.index("Chapecoense") + 1}º posição')
print('-=-' * 20)
