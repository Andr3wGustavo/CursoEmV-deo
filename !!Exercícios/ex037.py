# Conversor de bases
print('-='*15)
print('CONVERSOR DE BASE NÚMERICA')
print('-='*15)
num = int(input('Digite um número inteiro: '))
print('[1] Binário\n[2] Octal\n[3] Hexadecimal')
escolha = int(input('Escolha a base de conversão:'))
binario = bin(num)  # Converte para binario
hexa = hex(num)  # Converte para hexadecima
octal = oct(num)  # Converte para octal
if escolha == 1:
    print('O número {} em Binário é:{} '.format(num, binario[2:]))  # [2:] Começa da parte que interessa
elif escolha == 2:
    print('O número {} em Octal é:{} '.format(num, octal[2:]))
elif escolha == 3:
    print('O número {} em Hexadecimal é:{}'.format(num, hexa[2:]))
else:
    print('Você não escolheu uma conversão valída!')



