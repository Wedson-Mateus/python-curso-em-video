pessoa = {}
pessoas = []
soma = media = 0
acima_da_media = []

while True:
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo (M/F): ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break

    pessoa['idade'] = int(input('Idade: '))

    while True:
        cont = str(input('Deseja continuar (S/N): ')).upper().strip()[0]
        if cont in 'SN':
            break
    pessoas.append(pessoa.copy())
    soma += pessoa['idade']
    if cont == 'N':
        break
print('=' * 30)

print(f'O grupo tem {len(pessoas)}', 'pessoas' if len(pessoas) > 1 else 'pessoa')

media = soma / len(pessoas)
print(f'A média de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

print(f'Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('<< ENCERRADO >>')
