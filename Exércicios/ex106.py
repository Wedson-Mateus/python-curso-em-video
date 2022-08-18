def escreva(msg):
    tamanho = len(msg)
    print('-' * tamanho)
    print(f'{msg:^{tamanho}}')
    print('-' * tamanho)


def ajuda():
    from time import sleep

    while True:
        print(f'\033[0;0;42m', end='')
        escreva('Sistema de ajuda PyHELP')
        pergunta = str(input('\033[mFunção ou Biblioteca: ')).strip()

        if pergunta in 'FIM' or pergunta in 'fim':
            print('\033[0;0;41m', end='')
            escreva('ATÉ LOGO')
            break
        else:
            print('\033[0;31;46m', end='')
            escreva(f"Acessando o manual do comando '{pergunta}'")
            sleep(1)
            print('\033[7;30m')
            help(pergunta)


ajuda()
