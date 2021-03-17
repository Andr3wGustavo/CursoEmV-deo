# Verificador de número impar ou par
num = int(input('Digite um número qualquer: '))
verifica = num%2  # pega o resto da divisão
if verifica == 0:  # Se o resto da divisão da 0, é pq é um número par
    print('O número {} é par!'.format(num))
else:
    print('O número {} é impar!'.format(num))

