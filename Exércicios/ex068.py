from random import randint
cont = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    soma = jogador + computador
    op = ' '
    while op not in 'PI':
        op = str(input('Par ou Ímpar [P/I]? ')).upper().strip()[0]
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}')
        print(f'DEU PAR' if soma % 2 == 0 else 'DEU PAR')
    if op == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif op == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENCEU!')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            break
        print('Vamos jogar novamente...')
print(f'GAMER OVER! Você venceu {cont} vezes')
