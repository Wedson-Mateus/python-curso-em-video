salario = float(input('Qual é o sálario do funcionario? R$ '))
novo = salario + (salario * 15 / 100)
print(f'Um funcionario que ganhava R${salario:.2f}, com o aumento de 15% passa a ganhar R${novo:.2f}')
