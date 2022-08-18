matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma_coluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        if matriz[linha][2] >= 0:
            soma_coluna += matriz[linha][2]

print('-=' * 15)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()

print('-=' * 15)
print(f'O resultado da soma dos valores pares é: {pares}')
print(f'O resultado da soma dos valores da terceira coluna é: {soma_coluna}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
