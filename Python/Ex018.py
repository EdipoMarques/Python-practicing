
from math import radians, sin, cos, tan

angle = float(input('Enter here the angle: '))
seno = sin(radians(angle))
cosseno = cos(radians(angle))
tangente = tan(radians(angle))
print(f"O ângulo de {angle} tem o SENO de {seno}")
print(f"O ângulo de {angle} tem o COSSENO de {cosseno} ")
print(f"O ângulo de {angle} tem a TANGENTE de {tangente}")
