while True:
    num = int(input('De qual número você quer ver a tabuada? '))
    if num < 0:
        break
    print(f'Tabuada do número {num}')
    for n in range(1, 11):
        print(f'{num} X {n} = {num * n}')
print('PROGRAM TEBUADA ENCERRADO. Volte sempre')
