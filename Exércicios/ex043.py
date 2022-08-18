peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em Metros: '))
imc = peso / (altura * altura)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('VocÊ está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com Sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com Obesidade!')
else:
    print('Você está com Obsidade Mórbida!')
