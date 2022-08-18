def fatorial(fac, show=False):
    """

    -> Calcula o fatorial de um número.
    :param fac: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: O valor do fatorial de um número fac
    """
    f = 1
    for c in range(fac, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print('-' * 30)
print(fatorial(5, True))
