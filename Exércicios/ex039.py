from datetime import date  # importando a biblioteca dateime.

sexo = int(input('''Informe o seu sexo?
[ 1 ] Masculino
[ 2 ] Feminino 
Opção: '''))
if sexo == 1:
    ano = int(input('Em qual ano você nasceu? '))
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade > 18:
        saldo = idade - 18
        print('Você ja passou {} ano(s) da data do seu alistamento.'.format(saldo))
        data = ano_atual - saldo
        print('O seu ano de alistamento era {}.'.format(data))
    elif idade < 18:
        saldo = idade - 18
        print('Ainda faltam {} ano(s) para o alistamento.'.format(saldo))
        data = ano_atual + saldo
        print('O seu ano de alistamento será {}.'.format(data))
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')
elif sexo == 2:
    print('Você não precisa se alistar!')
