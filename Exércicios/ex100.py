from random import randint
from time import sleep


def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        lista.append(randint(0, 10))

    for s in lista:
        sleep(0.5)
        print(f'{s}', end=' ')
    print('PRONTO!')


def somapar(lista_0):
    pares = 0
    for nu in lista_0:
        if nu % 2 == 0:
            pares += nu
    print(f'Somando os valores pares de {lista_0}, temos {pares}')


numeros = []
sorteio(numeros)
somapar(numeros)
