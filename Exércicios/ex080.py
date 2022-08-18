valores = []  # criando uma lista vazia para receber os valores
for i in range(0, 5):  # Iniciando o loop com a quantidade de valores
    num = int(input('Digite um valor: '))  # Pedido para o usuario digitar os valores
# Verificando se os valores onde o primeiro valor vai ser incerido, e se o proximo será maior do que o ultimo
    if i == 0 or num > valores[-1]:
        valores.append(num)  # Adicionado o valor a lista já no seu lugar
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):  # Loop para verificar a posição dos demais valores
            if num <= valores[pos]:  # Identificando a posição
                valores.insert(pos, num)  # Inserindo na posição certa
                print(f'Adicionado a posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores em ordem foram {valores}')
