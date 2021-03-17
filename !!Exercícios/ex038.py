# Comparador entre dois números
print('-=' * 12)
print('COMPARADOR DE NÚMEROS')
print('-=' * 12)
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('O número {} é maior que o número {}'.format(num1, num2))
elif num2 > num1:
    print('O número {} é maior que o número {}'.format(num2, num1))
else:
    print('O número {} é igual ao número {}'.format(num1, num2))
