"""from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')"""

"""resultado = 1
cont = 1
número = int(input('Fatorial de: '))
while cont <= número:
    resultado *= cont
    cont += 1
print(resultado)"""

"""resultado = 1
número = int(input('Fatorial de: '))
for n in range(1, número+1):
    resultado *= n
print(resultado)"""

n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
