# Varios números com flag, fiz sem ver a aula do guanabra, jeito mais burro
num = 0
soma = 0
contador = -1
while num != 999:  # so executa o codigo enquanto o num digita for diferente de 999
    num = int(input('Digite um valor (999 para parar): '))
    contador += 1  # a cada vez q o codigo roda ele soma 1
    if num != 999:
        soma += num  # a cada número diferente de 999 digitado, ele acumula os valores
print('A soma dos {} valores foi {}!'.format(contador, soma))
