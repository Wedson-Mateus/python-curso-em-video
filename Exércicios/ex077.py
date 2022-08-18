palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programar', 'futuro')
for pos in palavras:
    print(f'\nNa palavra {pos.upper()} temos ', end='')
    for letras in pos:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
