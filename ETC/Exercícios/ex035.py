# Analisador de triangulo

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('-='*12)
print('ANALISADOR DE TRIÂNGULO')
print('-='*12)
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b + c and b < c + a and c < a + b:
    # Basicamente se a soma de dois lados forem menor que um dos lados, não pode se formar triagulo
    # Mas se a soma de dois segmentos forem maior que um segmento, pode se formar triangulo
    print('O segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')

