from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
opcao = 0
while opcao != 5:
    opcao = int(input('''Escolha uma das opção: 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa 
    '''))
    sleep(2)
    if opcao == 1:
        soma = n1 + n2
        print(f'O resultado de {n1} + {n2} é {soma}')
    elif opcao == 2:
        multiplicao = n1 * n2
        print(f'O resultado de {n1} * {n2} é {multiplicao}')
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior é {n1}')
        else:
            print(f'Entre {n1} e {n2} o maior é {n2}')
    elif opcao == 4:
        n1 = int(input('Digite o novo número: '))
        n2 = int(input('Digite mais um novo número: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(5)
    else:
        print('Opção inválida, escolha um opçao valida')
