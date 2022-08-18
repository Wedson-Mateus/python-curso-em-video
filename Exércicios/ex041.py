from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento? '))
idade = atual - nascimento
print('O atleta tem () anos'.format(idade))
if idade <= 9:
    print('Sua categoria é a MIRIM.')
elif idade <= 14:
    print('Sua categoria é a INFANTIL.')
elif idade <= 19:
    print('Sua categoria é a JÚNIOR.')
elif idade <= 25:
    print('A sua categoria é a SÊNIOR.')
else:
    print('A sua categoria é a MASTER.')
