# Jeito do guanabara de resolver o exercicio 52
vermelho = '\033[31m'
verde = '\033[32m'
limpa = '\033[m'
total = 0
num = int(input('Digite um número: '))
for x in range(1, num + 1):  # Faz os comandos rodarem conforme o número do input
    if num % x == 0:  # Se o número for divisivel por algum número dentro do intervalo 0 -> num, mostra em verde
        print('{}{}{}'.format(verde, x, limpa), end=' ')
        total += 1  # A cada vez que o num for divisivel ele soma 1x
    else:  # Se o num não for divisivel ele mostra em vermelho
        print('{}{}{}'.format(vermelho, x, limpa), end=' ')
print('\nO número {} foi divisivel {} vezes,'.format(num, total), end=' ')
if total == 2:  # Se o número for divisivel num total de 2x, significa que ele é primo
    print('e por isso ele é PRIMO!')
else:  # Se o num for divisivel mais de 2x ele não é primo
    print('e por isso ele NÃO É PRIMO!')
