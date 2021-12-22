#Calculadora de seno, cosseno e tangente de um ângulo
from  math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno de {}° é {:.2f}'.format(angulo, seno))
print('O cosseno de {}° é {:.2f}'.format(angulo, cosseno))
print('A tangente de {}° é {:.2f}'.format(angulo, tangente))
