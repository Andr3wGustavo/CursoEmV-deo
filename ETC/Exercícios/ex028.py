# Jogo entre o pc e o jogador
from random import randint
print('-=-'*17)
print('Vou pensar em um número de 0 a 5, tente adivinhar!')
print('-=-'*17)
num = int(input('Digite um número: '))
pc = randint(0,5)  # Faz o pc gerar um número aleatorio de 0 a 5
if num == pc:  # Se o número do player for igual ao do pc, voce ganha
    print('Parabéns, você consegiu adivinhar!')
else:  # Se o numero do player for diferente do pc, voce perde
    print('Perdeu, eu pensei no número {}, e não no {}.'.format(pc, num))
