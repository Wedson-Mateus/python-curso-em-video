primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 9) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' → ')
print('ACABOU')
