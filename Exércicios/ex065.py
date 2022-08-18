resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar[S/N]: ')).strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a medida deles é de {media}')
print(f'O maior valor analisado foi {maior} e o menor foi {menor}')
