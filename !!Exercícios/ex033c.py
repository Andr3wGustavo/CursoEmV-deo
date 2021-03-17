# Terceira forma de fazer o exercicio 33
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
lista = sorted([num1, num2, num3])  # Cria uma lista do menor para o maior, rearanja os números
print('O maior número é o {}'.format(lista[2]))
print('O menor número é o {}'.format(lista[0]))
