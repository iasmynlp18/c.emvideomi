from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo: '))
rad = radians(ang)
sen = sin(rad)
cos = cos(rad)
tang = tan(rad)
print(f'O angulo de {ang} tem o SENO: {sen:.2f} \nO angulo de {ang} tem o COSSENO: {cos:.2f} \nO angulo de {ang} tem a TANGENTE: {tang:.2f} ')