def aumentar(n=0, p=0):
    porcentagem = p / 100
    mais = n + (n * porcentagem)
    return mais


def diminuir(n=0, p=0):
    porcentagem = p / 100
    menos = n - (n * porcentagem)
    return menos


def dobro(n=0):
    dob = n * 2
    return dob


def metade(n=0):
    met = n / 2
    return met


def moeda(fun=0, sigla='R$'):
    formatado = f'{sigla}{fun:.2f}'.replace('.', ',')
    return formatado
