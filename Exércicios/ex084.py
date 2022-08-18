dados = []
galera = []
pesos = []
maior = []
menor = []

while True:
    dados.append(str(input('Digite o seu nome: ')).title())
    dados.append(int(input('Digite o seu peso: ')))
    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    galera.append(dados[:])
    dados.clear()
    print('-' * 30)

    while resp not in 'SN':
        resp = str(input('Deseja contiuar [S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break

print(f'Foram cadastradas {int(len(galera))} Pessoas')

for p in range(0, int(len(galera))):
    if galera[p][1] >= galera[p][1]:
        pesos.append(galera[p][1])
        if max(pesos) == galera[p][1]:
            maior = galera[p][0]
        if min(pesos) == galera[p][1]:
            menor = galera[p][0]

print(f'O maior peso foi de {max(pesos):.1f}Kg. Peso de {maior}')
print(f'O menor peso foi de {min(pesos):.1f}Kg. Peso de {menor}')
