num_temp = []
num = [[], []]

for n in range(0, 7):
    num_temp.append(int(input(f'Digite o {n + 1}° número: ')))
    if num_temp[n] % 2 == 0:
        num[0].append(num_temp[n])
    elif num_temp[n] % 2 == 1:
        num[1].append(num_temp[n])

print(f'Esses são os números pares em ordem crescente {sorted(num[0])}')
print(f'Esses são os números impares em ordem decresente {sorted(num[1])}')
