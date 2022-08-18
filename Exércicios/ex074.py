"""from random import sample
numeros = sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
sorteados = (numeros)
print(f'Os valores sorteados foram: {sorteados}')
print(f'O maior valor sorteado foi {max(sorteados)}')
print(f'O menor valor sorteado foi {min(sorteados)}')"""

from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end=' ')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
