# Tabuada do até o 10 utilizando laço for
num = int(input('Digite um número: '))
x = 0
for c in range(num, num * 11, num):  # Começa em numero, repete 10x, pulando de numero em numero
    x += 1  # a cada vez q ele repete, é adicionado o valor do número, formando a tabuada
    print('{}x{} = {}'.format(num, x, c))
