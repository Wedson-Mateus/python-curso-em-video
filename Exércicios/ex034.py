salario = float(input('Qual o valor do seu salario? R$'))
if salario <= 1250:
    sn = (salario * 0.15) + salario
# salario = salario + (salario * 15 / 100) essa é a forma que o professor usa para resolver porcentagem.
    print('O seu salario com o aumento de 15% será de {:.2f}'.format(sn))
else:
    sn = (salario * 0.10) + salario
# salario = salario + (salario * 10 / 100) essa é a forma que o professor usa para resolver porcentagem.
    print('O seu salario com o aumento de 10% será de {:.2f}'.format(sn))
