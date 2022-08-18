num = int(input('Digite um número para saber a sua tabuada: '))
print('=-' * 20)
print(f'Tabuada do número {num}')
for c in range(1, 11):
    print(f'{num} X {c} = {num * c}')
print('=-' * 20)
