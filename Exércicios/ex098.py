from time import sleep


def contador(inicio, fim, passos):
    if passos < 0:
        passos *= -1

    if passos == 0:
        passos = 1

    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passos} em {passos}')
    sleep(1.5)

    if inicio < fim:
        cont = 0
        while cont <= fim:
            sleep(0.5)
            print(f'{cont}', end=' ')
            cont += passos
        print('FIM!')

    else:
        cont = inicio
        while cont >= fim:
            sleep(0.5)
            print(f'{cont}', end=' ')
            cont -= passos
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fimm = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fimm, passo)
