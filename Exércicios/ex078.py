maior = menor = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=-' * 24)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} e está nas posiçãos ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} e está nas posiçãos ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()
