# Segunda solução do exercicio 33
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número?: '))
numeros = [num3, num2, num1]
print('O maior número é o {}'.format(max(numeros)))  # o max verifica qual o maior numero dentro da lista
print('O menor número é o {}'.format(min(numeros)))  # o min  verifica qual o menor numero dentro da lista
