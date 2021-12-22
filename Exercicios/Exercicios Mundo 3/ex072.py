
numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('Digite um numero entre 0 e 20: '))
        if 20 >= num >= 0:
            break
        print('Tente novamente, opção invalida!')
    print(f'Voce digitou o numero {numeros[num]}')
    continua = str(input('Voce quer continuar? [N/S]: '))
    if continua == 'N':
        break



