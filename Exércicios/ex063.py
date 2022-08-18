"""proximo = 0
anterior = 0
while proximo < 50:
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo = proximo + 1"""

print('-=' * 30)
print('Sequência Finonacci')
print('-=' * 30)
n = int(input('Quantos termos você deseja mostrar: '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
