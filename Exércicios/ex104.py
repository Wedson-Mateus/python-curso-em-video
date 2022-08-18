def leiaint(msg):
    ok = False
    valor = 0

    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True

        else:
            print('\033[0;31mERROR! Digite um número inteiro valído.\033[m')

        if ok:
            break

    return valor


num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número \033[0;32m{num}\033[m')
