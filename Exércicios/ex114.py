import requests


def conexao():
    url = 'http://www.pudim.com.br'
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.exceptions.ConnectionError:
        return False


if conexao():
    print('\033[0;32mConsegui acessar o site Pudim com sucesso.\033[m')

else:
    print('\033[0;31mO site Pudim não está acessivel nesse momento.')


# Resolução do professor
'''import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')

else:
    print('Consegui acessar o site Pudim com sucesso!')'''