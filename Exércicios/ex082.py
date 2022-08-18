valores_totais = []
valores_impares = []
valores_pares = []

while True:
    valores_totais.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

    if continuar == 'N':
        break

for valores in valores_totais:
    if valores % 2 == 0:
        valores_pares.append(valores)
    elif valores % 2 == 1:
        valores_impares.append(valores)

print(f'A lista completa fica assim {valores_totais}')
print(f'Essa é a lista com os valores pares {valores_pares}')
print(f'Essa é a lista com os valores impares {valores_impares}')
