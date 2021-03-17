num = 1
par = impar = 0
while num != 0:  # Executa o codigo até receber 0 no input
    num = int(input('Digite um valor: '))
    if num != 0:  # Elimna o 0 da contagem, pois senao ele iria contar o zero como par
        if num % 2 == 0:  # Verifica se o número é par, se for ele soma mais um valor a 'par'
            par += 1
        else:  # Se não for par, naturalmente é impar, e é adicionado um valor a 'impar'
            impar += 1
print('Você digitou {} números pares e {} números impares!'.format(par, impar))