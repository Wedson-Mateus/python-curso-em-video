from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
ranking = []

for n in range(0, 4):
    jogadores[f'jogador{n + 1}'] = randint(1, 6)

print('Valores sorteados: ')

for v, k in jogadores.items():
    print(f'\t{v} tirou {k}')
    sleep(1)

print('Ranking dos jogadores: ')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'\t{i + 1}º lugar: {v[0]} tirou {v[1]}')

# for p, j in enumerate(sorted(jogadores, key=jogadores.get, reverse=True)):
#    print(f'\t{p + 1} lugar: {j} tirou {jogadores[j]}')
