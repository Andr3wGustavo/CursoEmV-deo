# Tratando varios números
contador = -1  # incializa com -1 pra anular o 999
soma = 0
n = 0
while n != 999:  # enquanto o usuario não digitar '999' o programa roda
    n = int(input('Digte um número [999 para parar]: '))
    contador += 1  # conta quantas vezes o programa rodou
    if n != 999:  # o programa so irá somar se o valor de n for diferente de 999
        soma += n
    else:  # mas se n for igual a 999, ele ira finalizar
        print('Finalizando...')
print('Você digitou {} e a soma entre eles foi {}'.format(contador, soma))

