# JOKEMPO com o pc
from random import randint
limpa = '\033[m'
azul = '\033[34m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
magenta = '\033[35m'
ciano = '\033[36m'
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
print('{}-={}'.format(ciano, limpa) * 12)
print('  {}Jokempô contra o PC{}'.format(azul, limpa))
print('{}-={}'.format(ciano, limpa) * 12)

computador = randint(1, 3)  # Gera um número para o computador
jogador = int(input('''{}[1]{} Papel\n{}[2]{} Tesoura\n{}[3]{} Pedra\nDigite sua escolha: '''.
                    format(amarelo, limpa, amarelo, limpa, amarelo, limpa)))
# Mostra na tela a escolha do computador, de acordo com o número que ele randomizou
# Só mostra na tela se a escolha do jogador for valida
if 4 > jogador >= 1:
    if computador == 1:
        escolha_computador = 'Papel'
        print('Computador escolheu: {}{}{}'.format(magenta, escolha_computador, limpa))
    elif computador == 2:
        escolha_computador = 'Tesoura'
        print('Computador escolheu: {}{}{}'.format(magenta, escolha_computador, limpa))
    elif computador == 3:
        escolha_computador = 'Pedra'
        print('Computador escolheu: {}{}{}'.format(magenta, escolha_computador, limpa))
else:
    print('{}Você fez uma escolha valída, tente novamente!{}'.format(vermelho, limpa))
# Mostra na tela a escolha do computador
if jogador == 1:
    escolha_jogador = 'Papel'
    print('Você escolheu: {}{}{}'.format(magenta, escolha_jogador, limpa))
elif jogador == 2:
    escolha_jogador = 'Tesoura'
    print('Você escolheu: {}{}{}'.format(magenta, escolha_jogador, limpa))
elif jogador == 3:
    escolha_jogador = 'Pedra'
    print('Você escolheu: {}{}{}'.format(magenta, escolha_jogador, limpa))
# estabelece mos critérios de derrota ou vitória
if jogador == 1 and computador == 2 or jogador == 2 and computador == 3 or jogador == 3 and computador == 1:
    print('{}Você PERDEU!{}'.format(vermelho, limpa))
elif jogador == 3 and computador == 2 or jogador == 2 and computador == 1 or jogador == 1 and computador == 3:
    print('{}Você GANHOU!{}'.format(verde, limpa))
elif jogador == computador:
    print('{}EMPATE!{}'.format(amarelo, limpa))

