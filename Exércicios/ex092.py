from datetime import date
# from datetime import datetime

funcionario = dict()

funcionario['nome'] = str(input('Nome: ')).title()

ano_de_nascimento = int(input('Ano de Nascimento: '))
ano_atual = date.today()  # datetime.now().year - ano_de_nascimento
funcionario['idade'] = ano_atual.year - ano_de_nascimento

funcionario['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if funcionario['ctps'] > 0:
    funcionario['contratacão'] = int(input('Ano de contratação: '))

    funcionario['salario'] = float(input('Salário: '))

    funcionario['aposentadoria'] = funcionario["contratacão"] + 35 - ano_de_nascimento

print('-=' * 15)
for k, v in funcionario.items():
    print(f'{k.title()} tem o valor {v}')
