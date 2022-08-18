ficha_alunos = []
notas = 0

while True:
    nome = str(input('Nome: ')).title()
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha_alunos.append([nome, [nota_1, nota_2], media])

    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]

    if resp == 'N':
        break

print('-=' * 15)
print(f'{"No.":<2}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 18)

for i, n in enumerate(ficha_alunos):
    print(f'"{i:<2}{n[0]:<10}{n[2]:>8.1f}"')
print('-' * 35)

while True:
    print('-' * 35)
    notas = int(input('Mostra notas de qual aluno? (999 interrompe): '))
    if notas == 999:
        print('FINALIZANDO...')
        break
    if notas <= len(ficha_alunos) - 1:
        print(f'Notas de {ficha_alunos[notas][0]} são {ficha_alunos[notas][1]}')

print('<<< VOLTE SEMPRE >>>')
