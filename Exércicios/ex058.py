"""from random import randint
from time import sleep
tentativa = 0
computador = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 10, Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
while not jogador == computador:
    jogador = int(input('Tente de novo, Em qual número eu pensei? '))
    if jogador == computador:
        tentativa += 1
print(f"PARABÉNS você ganhou,eu pensei no número {computador} e você adivinhou,"
      f" você tentou {tentativa} veze(s) até acertar")"""

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número de 0 a 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez: ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez: ')
print(f'Acertou com {palpites} tentativas. Parabéns!')
