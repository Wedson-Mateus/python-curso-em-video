valor = float(input('Digite o valor do produto: R$'))
pagamento = int(input('''Escolha a forma de pagamento:
[1] Avista dinheiro/cheque
[2] Avista no cartão 
[3] Dividido no cartão 
'''))
if pagamento == 1:
    desconto = valor - (valor * 10 / 100)
    print('O valor que você pagarà no produto com o desconto de 10% é de R${}.'.format(desconto))
elif pagamento == 2:
    desconto = valor - (valor * 5 / 100)
    print('O valor que você pagara no produto com o desconto de 5% é de R${}.'.format(desconto))
elif pagamento == 3:
    parcelas = int(input('Em quantas parcelas você vai dividir a sua compra: '))
    if parcelas == 2:
        print('Não será combrado juros na sua compra, então você pagará R${} pelo produto'.format(valor))
    elif parcelas >= 3:
        juros = valor + (valor * 20 / 100)
        print('O produto terá um acrecimo de 20%, então você pagara R${} pelo produto.'.format(juros))
else:
    print('Opção invalída, escolha um dos números acima!')
# Para centralizar usa-se '{:^}'.
