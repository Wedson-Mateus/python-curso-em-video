from time import sleep


def maior(* numeros):
    cont = v_maior = 0

    sleep(0.8)
    print('-=' * 30)
    print('Analisando os valores passados...')

    for n in numeros:
        # v_maior = max(numeros)
        if cont == 0:
            v_maior = n
        else:
            if n > v_maior:
                v_maior = n
        cont += 1
        
        print(f'{n}', end=' ')
        sleep(0.5)
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi {v_maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
