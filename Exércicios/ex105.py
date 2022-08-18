def notas(* n, sit=False):
    """

    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notos dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com varias informações sobre a situação da turma
    """
    cont = maior = menor = soma = 0

    for c in n:
        if cont == 0:
            maior = menor = c
        else:
            if c > maior:
                maior = c

            if c < menor:
                menor = c
        cont += 1
        soma += c
    media = soma / len(n)
    if sit:
        if media < 5:
            ficha = {'total': len(n), 'maior': maior, 'menor': menor, 'media': media, 'situacao': 'RUIM'}
            return ficha

        elif 5 <= media < 7:
            ficha = {'total': len(n), 'maior': maior, 'menor': menor, 'media': media, 'situacao': 'RAZOAVEL'}
            return ficha

        else:
            ficha = {'total': len(n), 'maior': maior, 'menor': menor, 'media': media, 'situacao': 'BOA'}
            return ficha

    else:
        ficha = {'total': len(n), 'maior': maior, 'menor': menor, 'media': media}
        return ficha


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
