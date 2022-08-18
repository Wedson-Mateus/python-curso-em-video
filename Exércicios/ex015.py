dias = int(input('Quantos dias eu alugado? '))
km = float(input('Quantos KMs rodados? '))
pago = (60 * dias) + (0.15 * km)
print(f'O total a pagar é de R${pago}')
