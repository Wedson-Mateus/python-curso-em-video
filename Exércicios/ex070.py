soma = totmil = cont = menor = 0
barato = ' '
while True:
    print('-' * 30)
    print(' ' * 5, 'LOJA DEV ECONOMICO')
    print('-' * 30)
    produto = str(input('Nome do produto: ')).upper().strip()
    valor = float(input('Preço: R$'))
    cont += 1
    soma += valor
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    resp = ' '
    while resp not in 'SN':
        print('-' * 30)
        resp = str(input('Dejesa comprar mais algum item [S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 5, 'FIM DO PROGRAMA', '-=' * 5)
print(f'O total da sua compra foi de R${soma:.2f}')
print(f'Você adquiriu {totmil} produtos acima de R$1000,00 reais')
print(f'O produto mais barato é o {barato} que custa R${menor:.2f}')
print('Obrigado pela prefêrencia, VOLTE SEMPRE!!!')
