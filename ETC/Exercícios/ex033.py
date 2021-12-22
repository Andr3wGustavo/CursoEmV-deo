# Qual é maior
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
maior = num1
menor = num1
if num2 > num1 and num2 > num3:
    maior = num2  # Se o num2 for maior que os outros ele passa a ser o a var maior
if num3 > num2 and num3 > num1:
    maior = num3
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3
print('O Maior número é o {}'.format(maior))
print('O menor número é o {}'.format(menor))
