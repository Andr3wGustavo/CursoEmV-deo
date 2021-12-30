a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b + c and b < c + a and c < a + b:
    if a == b == c:
        tipo = 'Equilatero'
    elif a == b or c == a or c == b:
        tipo = 'Isosceles'
    else:
        tipo = 'Escaleno'
    print(f'O segmentos acima PODEM formar um triângulo! O tipo do triângulo é {tipo}!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
