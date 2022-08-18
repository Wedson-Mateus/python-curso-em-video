"""listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.00, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 42)
print(' ' * 10, 'LISTAGEM DE PREÇOS')
print('-' * 42)
print(listagem[0], '.' * 25, 'R$', ' ' * 2, listagem[1])
print(listagem[2], '.' * 22, 'R$', ' ' * 2, listagem[3], end='0\n')
print(listagem[4], '.' * 23, 'R$', ' ' * 1, listagem[5], end='0\n')
print(listagem[6], '.' * 24, 'R$', ' ' * 1, listagem[7], end='0\n')
print(listagem[8], '.' * 19, 'R$', ' ' * 2, listagem[9], end='0\n')
print(listagem[10], '.' * 22, 'R$', ' ' * 2, listagem[11])
print(listagem[12], '.' * 23, 'R$', '' * 1, listagem[13], end='0\n')
print(listagem[14], '.' * 23, 'R$', ' ' * 1, listagem[15], end='0\n')
print(listagem[16], '.' * 25, 'R$', ' ' * 1, listagem[17], end='0\n')
print('-' * 42)"""
listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.00, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
