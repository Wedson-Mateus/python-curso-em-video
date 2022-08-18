def voto(ano_nascimento):
    """

     Recebe o ano de nascimento do usuario e retorna a idade, e se é obrigatorio, opcional, ou se ele(a)
     não precisa votar."""
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento

    if idade < 18:
        return f'Com {idade} anos: NÃO VOTA'

    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'

    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


print('-' * 30)
pergunta = int(input('Em que ano você nasceu? '))
print(voto(pergunta))
