contagem = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    resp = ' '
    if n < 0 or n > 20:
        print('INVALIDO TENTE NOVAMENTE.', end=' ')
    elif n >= 0 or n <= 20:
        print('◄►' * 15)
        print(f'Você digitou o número {contagem[n]}')
        print('◄►' * 15)
        while resp not in 'SN':
            resp = str(input('Você deseja continuar[S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('◄►' * 3, 'FIM DO PROGRAMA', '◄►' * 3)
