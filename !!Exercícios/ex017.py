#Calculadora de hipotenusa de um triangulo
from math import sqrt, pow, hypot

#Jeito normal
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = sqrt(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))
print('A hipotenusa do triângulo é {:.2f}'.format(hipotenusa))

#Jeito mais facil
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(hipotenusa)

