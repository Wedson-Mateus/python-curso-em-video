def leiaint(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('\033[0;31mError: Por favor, digite um número inteiro válido.\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0

        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))

        except ValueError:
            print('\033[0;31mError: Por favor, digite um número real válido.\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário prefiriu não digitar esse número.\033[m')
            return 0

        else:
            return n


inteiro = leiaint('Digite um número inteiro: ')
real = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi \033[0;32m{inteiro}\033[m e o real foi \033[0;32m{real}\033[m')
