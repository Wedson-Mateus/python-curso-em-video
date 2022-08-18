def leiadinheiro(dados):
    while True:
        da = str(input(dados)).replace(',', '.').strip()

        if da.isalpha() or da == '':
            print(f'\033[0;31mError: \"{da}\" é um preço inválido!\033[m')

        else:
            return float(da)
