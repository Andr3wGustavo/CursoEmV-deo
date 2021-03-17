# Desafio 028 melhorado
from random import randint
computador = randint(0, 10)
num = -1
palpites = 0
print('Pensei em um número entre 0  e 10, tente adivinhar!')
while num != computador:  # Enquanto o palpilte não for igual o computador, ele roda o codigo
    num = int(input('Qual é seu palpite? '))
    palpites += 1  # Contador de palpites
    if num > computador:  # Verifica se o palpite é maior que o computador
        print('Menos...Tente Novamente!')
    if num < computador:  # Verifica se o palpite é menor que o computador
        print('Mais...Tente Novamente!')
    if num == computador:  # Verifica se o número é o mesmo do computador
        print('Você acertou, parabéns!')
print('Você precisou de {} palpites para acertar!'.format(palpites))
