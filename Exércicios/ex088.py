from random import randint
from time import sleep
jogos = []
numeros = []

print('-' * 30)
print(f'{"JOGOS DA MEGA SENA":^30}')
print('-' * 30)

quantidade = int(input('Quantos jogos você quer gerar? '))
print('-=' * 3, f" SORTEANDO {quantidade} JOGOS ", '-=' * 3)

for quant in range(0, quantidade):
    while len(numeros) < 6:
        numero = randint(1, 60)
        if numero not in numeros:
            numeros.append(numero)
    if len(numeros) <= 6:
        jogos.append(numeros[:])
        numeros.clear()
    sleep(2)
    print(f'JOGO {quant + 1}: {sorted(jogos[quant])}')

print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
