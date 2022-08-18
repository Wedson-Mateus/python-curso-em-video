tot18 = toth = totm20 = 0
while True:
    print('-=' * 10)
    print('CADASTRE UMA PESSOA')
    print('-=' * 10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if idade > 18:
            tot18 += 1
        if sexo == 'M':
            toth += 1
        elif sexo == 'F' and idade < 20:
            totm20 += 1
    resp = ' '
    while resp not in 'SN':
        print('-' * 20)
        resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 5, 'FIM DO PROGRAMA', '-=' * 5)
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'E temos {totm20} mulheres com menos de 20 anos')
