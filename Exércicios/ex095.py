jogador = {}
jogadores = []
lista_gols = []
tot_gols = 0

while True:
    jogador.clear()
    lista_gols.clear()
    tot_gols = 0

    jogador['nome'] = str(input('Nome do jogador: ')).title()
    quant_partidas = int(input(f'Quantas partidas {jogador["nome"].title()} jogou? '))

    for j in range(0, quant_partidas):
        gol = int(input(f'Quantos gols na partida {j + 1}? '))
        lista_gols.append(gol)
        tot_gols += gol

    jogador['gols'] = lista_gols.copy()
    jogador['total'] = tot_gols
    jogadores.append(jogador.copy())

    cont = str(input('Deseja continuar (S/N)? ')).upper()[0]
    while cont not in 'SN':
        print('\33[0:31mERRO!\033[m\nDigite apenas S ou N.')
        cont = str(input('Deseja continuar (S/N)? ')).upper()[0]

    if cont == 'N':
        break

print('=-' * 30)
print(f'{"Cod"} ', end='')
for c in jogador.keys():
    print(f'{c.title():<15}', end='')
print()
print('-' * 50)

for contador, dados in enumerate(jogadores):
    print(f'{contador:<5}', end='')
    for dado in dados.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 50)
while True:
    visualizar_dados = int(input('Deseja mostrar os dados de qual jogador? '))

    if visualizar_dados == 999:
        break

    if visualizar_dados <= len(jogadores) - 1:
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[visualizar_dados]["nome"]}')
        for g in range(len(jogadores[visualizar_dados]["gols"])):
            print(f'No jogo {g + 1} fez {jogadores[visualizar_dados]["gols"][g]}',
                  'gol'if jogadores[g]['gols'] == 1 else 'gols')

    else:
        print(f'\33[0:31mERROR\33[m, Não exise jogador com o código {visualizar_dados}! Tente novamente')
    
    print('-' * 50)

print('\33[0:32m<<< VOLTE SEMPRE >>>')
