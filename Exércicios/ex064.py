núm = cont = soma = 0
núm = int(input('Digite um número [999 para encerrar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para encerrar]: '))
print(f'Você digitou {cont} e a soma entre eles foi {soma}.')
