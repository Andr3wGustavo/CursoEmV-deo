from random import randint

limpa = '\033[m'
azul = '\033[34m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
magenta = '\033[35m'
ciano = '\033[36m'

print('{}-={}'.format(ciano, limpa) * 12)
print('  {}Jokempô contra o PC{}'.format(azul, limpa))
print('{}-={}'.format(ciano, limpa) * 12)

escolhas = ('PAPEL', 'TESOURA', 'PEDRA')

computador = randint(0, 2)

print('''faça sua escolha!
[0] PAPEL
[1] TESOURA
[2] PEDRA''')
jogador = int(input('Qual você escolheu? '))

if jogador <= 2:
    print('-=' * 15)
    print('O jogador jogou {}'.format(escolhas[jogador]))
    print('O computador jogou {}'.format(escolhas[computador]))
    print('-=' * 15)
    if jogador == 0 and computador == 1 or jogador == 1 and computador == 2 or jogador == 2 and computador == 0:
        print('{}Você PERDEU!{}'.format(vermelho, limpa))
    elif jogador == 2 and computador == 1 or jogador == 1 and computador == 0 or jogador == 0 and computador == 2:
        print('{}Você GANHOU!{}'.format(verde, limpa))
    elif jogador == computador:
        print('{}EMPATE!{}'.format(amarelo, limpa))
else:
    print('{}Escolha Inválida!{} '.format(vermelho, limpa))
