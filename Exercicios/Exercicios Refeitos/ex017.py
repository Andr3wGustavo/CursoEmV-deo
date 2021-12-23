from math import sqrt

op = float(input('Digite o valor do cateto oposto: '))
ad = float(input('Digite o valor do cateto adjacente: '))
print(f'O valor da hipotenusa é {sqrt(op**2+ad**2)}')