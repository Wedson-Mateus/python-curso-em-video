frase = str(input('Digite algo: ')).upper().strip()
print('A sua frase tem {} letras A'.format(frase.upper().count('A')))
print('A primeira letra A está na posição {}'.format(frase.find('A')+1))
print('A ultima letra A está na posição {}'.format(frase.rfind('A')+1))
