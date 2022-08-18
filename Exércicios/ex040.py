n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Você foi REPROVADO, A sua média foi menor que 5.0.')
elif 5 <= media < 7:
    print('Você está de recuperação.')
else:
    print('PARABÉNS você está aprovado!!!')
