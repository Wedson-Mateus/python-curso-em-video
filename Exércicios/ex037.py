n = int(input('Qual o número você deseja converter? '))
print('Digite "1" para binário, "2" para octal, "3" para hexadecimal ')
opcao = int(input())
if opcao == 1:
    binario = str(bin(n)[2:])
    print('O número {} convertido em número binàrio fica assim {}.'.format(n, binario))
elif opcao == 2:
    octal = str(oct(n)[2:])
    print('O número {} convertido em número octal fica assim {}.'.format(n, octal))
elif opcao == 3:
    hexadecimal = str(hex(n)[2:])
    print('O número {} convertido em número hexadecimal fica assim {}.'.format(n, hexadecimal))
else:
    print('\033[31mOPÇÃO INVÁLIDA!!!')
