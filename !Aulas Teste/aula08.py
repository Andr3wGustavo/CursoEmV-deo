#import math
#num = int(input('Digite um Número:'))
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {:.2f}'.format(num, math.floor(raiz)))

from math import sqrt, floor
num = int(input('Digite um número: '))
sqrt = sqrt(num)
print('A raiz quadrada de {} é {} '.format(num, floor(sqrt)))

