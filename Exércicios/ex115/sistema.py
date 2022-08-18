from time import sleep
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoexite(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if resposta == 1:
        lerarquivo(arq)

    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mError! Digite uma opção válida!\033[m')
    sleep(2)
