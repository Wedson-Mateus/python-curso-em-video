sigla = 'R$'


def aumentar(n=0, p=0, form=False):
    porcentagem = p / 100
    mais = n + (n * porcentagem)
    if form:
        return f'{sigla}{mais:.2f}'.replace('.', ',')
    else:
        return mais


def diminuir(n=0, p=0, form=False):
    porcentagem = p / 100
    menos = n - (n * porcentagem)
    if form:
        return f'{sigla}{menos:.2f}'.replace('.', ',')
    else:
        return menos


def dobro(n=0, form=False):
    dob = n * 2
    if form:
        return f'{sigla}{dob:.2f}'.replace('.', ',')
    else:
        return dob


def metade(n=0, form=False):
    met = n / 2
    if form:
        return f'{sigla}{met:.2f}'.replace('.', ',')
    else:
        return met


def moeda(fun=0, siglaa='R$'):
    formatado = f'{siglaa}{fun:.2f}'.replace('.', ',')
    return formatado


def resumo(valor, aumento=10, desconto=5):
    print('-' * 35)
    print(f'Resumo do valor'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{desconto}% de desconto: \t{diminuir(valor, desconto, True)}')
    print('-' * 35)
