# Sequencia de fibonacci

print('-' * 30)
print('Senquência de Fibonacci')
print('-' * 30)
num = int(input('Quantos termos você quer mostrar? '))
termo1 = 0  # inicia o primeiro termo como sendo 0
termo2 = 1  # inicia o segundo termo como sendo 1
print('-' * 30)
print('{} ➞ {}'.format(termo1, termo2), end='')
cont = 3  # ja começa a contar apartir do terceiro termo, pois os outros dois ja foram definidos
while cont <= num:  # Roda o programa enquanto o numero pedido não for antigido
    termo3 = termo1 + termo2  # o terceiro termo é a soma dos dois anteriores
    print(' ➞ {}'.format(termo3), end='')
    termo1 = termo2  # a cada vez que o programa roda, o termo1 passa a ser o termo2
    termo2 = termo3  # a cada vez que o programa roda, o termo2 passa a aser o termo3
    cont += 1  # conta quantas vezes o programa ja rodou
print(' ➞ FIM!')
