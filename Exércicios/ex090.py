ficha = {}

nome = str(input('Nome: '))
media = float(input(f'Média de {nome.title()}: '))

ficha['nome'] = nome
ficha['media'] = media

if ficha['media'] >= 7:
    ficha['situacao'] = 'aprovado'
elif 5 <= ficha['media'] < 7:
    ficha['situacao'] = 'recuperação'
else:
    ficha['situacao'] = 'reprovado'

print(f'Nome igual a {ficha["nome"].title()}')
print(f'Média igual a {ficha["media"]}')
print(f'Situação é igual a {ficha["situacao"]}')
