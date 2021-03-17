# Jogo do par ou impar com o comupator
from random import randint
pc = randint(0, 10)
print('=-=' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 10)
resultado = ''  # Inicializa a variavel resultado como nula
contador = 0  # Iniciliza o contador de vitorias como nulo
while resultado != 'PERDEU!':  # O programa roda até o player perder
    player = int(input('Digite um valor: '))
    par_ou_impar = str(input('Par ou impar? [P/I] ')).strip().upper()
    if par_ou_impar == 'P' or par_ou_impar == 'I':  # So executa se o palpite for válido, ou seja deve ser 'P' ou 'I'
        if (player + pc) % 2 == 0:  # Estabelece o criterio de divisibildiade, divisivel por 2 é par
            print('=-=' * 10)
            print('''Você jogou {} e o computador jogou {}. Total de {}, DEU PAR!'''
                  .format(player, pc, player + pc))
            print('=-=' * 10)
            if par_ou_impar == 'P':  # Se o palpite foi 'P' o jogador vence o jogo, e ele roda denovo
                print('Você VENCEU!')
                print('Vamos jogar novamente...')
                print('=-=' * 10)
                resultado = 'VENCEU!'  # Estabelece o resultado, fazendo o jogo continuar
                contador += 1  # Conta mais uma vitoria para o jogador
                pc = randint(1, 10)  # Reinicializa o número jogado pelo computador
            elif par_ou_impar == 'I':  # Mas se o palpite foi 'I' o jogador perde, e o jogo finaliza
                print('Você PERDEU!')
                print('=-=' * 10)
                resultado = 'PERDEU!'  # Estabelece o resultado, como o jogador perdeu, o jogo acaba
        else:  # Se a soma do computador mais o player não for divisivel por 2, o numero é impar
            print('=-=' * 10)
            print('''Você jogou {} e o computrador jogou {}. Total de {}, DEU IMPAR!'''.
                  format(player, pc, player + pc))
            print('=-=' * 10)
            if par_ou_impar == 'I':  # Se o palpite for 'I' entao o player acertou, o jogo continua
                print('Você VENCEU!')
                print('Vamos jogar novamente...')
                print('=-=' * 10)
                resultado = 'VENCEU!'  # Mostra o resultado pro programa
                contador += 1  # Soma mais uma vitoria para o jogador
                pc = randint(1, 10)  # Reseta o número randomizado pelo computador
            elif par_ou_impar == 'P':  # Se o palpite for 'P' o jogador perdeu o jogo, e ele acaba
                print('Você PERDEU!')
                print('=-=' * 10)
                resultado = 'PERDEU!'  # Mostra pro pc que o jogo acabou
    else:  # Se o palpite for diferente de 'P' ou 'I', a resposta é inválida
        print('Tente novamente, Essa resposta não é válida!')
print('GAME OVER! Você venceu {} vezes'.format(contador))
