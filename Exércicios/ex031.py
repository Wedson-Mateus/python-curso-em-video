"""distancia = float(input('Qual a distancia do seu destino em km? '))
if distancia <= 200:
    passagem1 = distancia * 0.50
    print('O valor que você pagará de passagem é esse {}'.format(passagem1))
else:
    passagem2 = distancia * 0.45
    print('O valor que você pagará de passagem é esse {}'.format(passagem2))
# Como eu resolvi o exercicio."""

'''distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
# Primeira forma que o professor resolveu.'''

# Resolução com a forma simplificada do IF/ELSE
distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
