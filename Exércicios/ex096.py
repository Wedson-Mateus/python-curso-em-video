def area(larg, comp):
    dimensao = larg * comp
    print(f'A área de um terreno {largura}x{comprimento} é de {dimensao}m²')


print(f"{'Controle de Terrenos':^30}")
print('-' * 30)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)
