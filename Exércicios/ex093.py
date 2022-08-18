jogador = dict()
lista_gols = []
tot_gols = 0

jogador['nome'] = str(input('Nome do jogador: ')).title()
quant_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for j in range(0, quant_partidas):
    gol = int(input(f'Quantos gosl na partida {j + 1}? '))
    lista_gols.append(gol)
    tot_gols += gol

jogador['gols'] = lista_gols
jogador['total'] = tot_gols

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)

for k, v in jogador.items():
    if k == 'nome':
        print(f'O jogador {v} jogou {len(jogador["gols"])} partidas.')
    if k == 'gols':
        for g in range(0, len(jogador['gols'])):
            print(f'\t=>Na partida {g + 1}, fez {v[g]} gols.')
    else:
        print(f'Foi um total de {v} gols.')

'''Outra forma para somar a quantidade de gols poderia se criar um lista e armazenar os gols dentro dela e depois usar
sum() para somar todos os items presentes na lista'''
