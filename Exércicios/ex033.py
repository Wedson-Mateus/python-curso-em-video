"""import math
p = float(input('Digite o primeiro número: '))
s = float(input('Digite o segundo número: '))
t = float(input('Digite o terceiro número: '))
lista = [p, s , t]
print('O menor número é {}\n O maior número é {}'.format(min(lista), max(lista)))
# Resolução que eu encontrei nos comentarios do video"""

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o menor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
