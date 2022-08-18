casa = float(input('Qual o valor da casa que você deseja financiar? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
parcelas = int(input('Em quantos anos você deseja parcelar o emprestimo? '))
porcentagem = salario * 30 / 100
valor_parcelas = casa / (parcelas * 12)
if valor_parcelas <= porcentagem:
    print('''\033[32mO seu emprestimo no valor de R${:.2f} FOI APROVADO.
          \033[m\nO valor das parcelas será de R${:.2f}'''.format(casa, valor_parcelas))
else:
    print('\033[31mO seu emprestimo FOI NEGADO\033[m\nO valor das parcelas ultrapassa 30% do seu salário.')
