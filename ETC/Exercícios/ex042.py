# Analisador de triangulo 2.0
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b+c and b < a+c and c < a+b:  # Verifica se é possivel formar triangulo
    print('É possivel formar triângulo com esses semgmentos!', end='')
    if a == c == b:
        print('O triângulo formado é EQUILÁTERO!')
    elif a == c or c == a or c == b:
        print('O triâgulo formado é ISÓSCELES!')
    elif a != b != c != a:
        print('O triâgulo formado é ESCALENO!')
else:
    print('Não é possivel formar triângulo com esses segmentos!')
