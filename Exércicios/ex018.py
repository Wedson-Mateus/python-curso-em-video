"""import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o SENO de {seno}:.2f}')
cosseno = math.cos(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem a COSSENO de {cosseno:.2f}')
tangente = math.tan(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f}')"""

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem COSSENO de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')
