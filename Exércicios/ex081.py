numeros = []
while True:
    numero = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    numeros.append(numero)

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar in 'N':
        break

print(f'Foi digitado {len(numeros)} número' if len(numeros) <= 1 else f'Foram digitados {len(numeros)} números')
numeros.sort(reverse=True)
print(f'Essa é a ordem decrescente dos valores {numeros}'if len(numeros) >= 2
      else f'Essa é a ordem descrescente dos valores {numero}')
print('O valor 5 ESTÁ na lista' if 5 in numeros else 'O valor 5 NÃO ESTÁ na lista')
