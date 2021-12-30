from random import choice
from time import sleep

pc = choice(['PEDRA', 'PAPEL', 'TESOURA'])
opc = int(input('Suas opções:\n'
                '[0] PEDRA\n'
                '[1] PAPEL\n'
                '[2] TESOURA\n'
                'Qual a sua jogada? '))

if opc == 0: escolha = 'PEDRA'
elif opc == 1: escolha = 'PAPEL'
else: escolha = 'TESOURA'

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)

print('-=' * 10)
print(f'Computador jogou {pc}')
print(f'Jogador jogou {escolha}')
print('-=' * 10)

if opc == 0 and pc == 'TESOURA' or opc == 1 and pc == 'PEDRA' or opc == 2 and pc == 'PAPEL':
    result = 'JOGADOR VENCE'
elif escolha == pc:
    result = 'EMPATE'
else:
    result = 'COMPUTADOR VENCE'

print(result)
