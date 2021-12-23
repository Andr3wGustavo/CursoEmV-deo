from math import sin, cos, tan, radians

ang = float(input('Digite o valor de um angulo: '))
print('O valor do seno: {:.2f}'.format(sin(radians(ang))))
print('O valor do cosseno: {:.2f}'.format(cos(radians(ang))))
print('O valor da tangente: {:.2f}'.format(tan(radians(ang))))