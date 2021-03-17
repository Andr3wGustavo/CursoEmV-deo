# Leitor de número primo, minha primeira tentativa, n ficou muito simples, mas funciona
limpa = '\033[m'
verde = '\033[32m'
vermelho = '\033[31m'
ciano = '\033[36m'

num = int(input('Digite um número: '))
#  Basicamente, estabelece os criterios de divisibilidade de um número primo
if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
    print('{}O número é PRIMO!{}'.format(ciano, limpa))
    for c in range(1, num + 1):
        if num % c == 0:  # Mostra por qual número do range, o número foi divisivel
            print('{}'.format(verde), end=' ')
        else:
            print('{}'.format(vermelho), end=' ')
        print(c, end=' ')
else:
    print('{}O número NÃO É PRIMO!{}'.format(ciano, limpa))
    for c in range(1, num + 1):
        if num % c == 0:
            print('{}'.format(verde), end=' ')
        else:
            print('{}'.format(vermelho), end=' ')
        print(c, end=' ')
