# Jogo de par ou impar entre o computador e o player
from random import randint  # exporta a biblioteca para gerar numeros aleatorios
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
vitorias = 0  # inicializa o contador de vitorias
while True:  # roda o codigo infinitamente
    pc = randint(0, 10)   # gera numeros aleatorios para o computador
    player = int(input('Digite um número: '))
    palpite = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    if palpite == 'P' or palpite == 'I':  # só executa se o usuario digitar um comando valido
        if (player + pc) % 2 == 0:  # se a soma do player e pc forem pares, ou seja divisiveis por 2
            resultado = 'P'  # resultado passa a ser par
            print('-=' * 15)
            print(f'Você jogou {player} e computador {pc}. Total de {player+pc} DEU PAR!')
            print('-=' * 15)
        else:  # se não for par, significa que é impar
            resultado = 'I'  # resultado passa a ser impar
            print('-='*15)
            print(f'Você jogou {player} e computador {pc}. Total de {player+pc} DEU ÍMPAR!')
        if palpite == resultado:  # se o palpite for igual o resultado, vitoria
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('-=' * 15)
            vitorias += 1  # soma mais um vitoria no contador
        else:  # se o resultador não for igual ao palpite, derrota
            print(f'GAMEOVER! Você venceu {vitorias}')
            break  # quebra o loop infinito na derrota
    else:  # se o usuario digitar um comando invalido no palpite
        print('Comando Inválido, Tente novamente!')


