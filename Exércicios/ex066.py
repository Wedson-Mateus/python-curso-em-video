soma = cont = 0
while True:
    n = int(input('Digite um número [999 para encerrar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} e a soma entre eles é de {soma}')
