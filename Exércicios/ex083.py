pilha = []
expressao = str(input('Digite a expressâo: '))

for s in expressao:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Expressâo VALÍDA!!!')
else:
    print('Expressão INVALÍDA!!!')
