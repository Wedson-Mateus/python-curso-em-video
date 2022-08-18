"""c = str(input('Qual o nome da cidade onde você mora: ')).strip().split()
print(c[0].upper() == 'SANTO')"""

cid = str(input('Qual o nome da cidade onde você mora: ')).strip()
print(cid[:5].upper() == 'SANTO')
