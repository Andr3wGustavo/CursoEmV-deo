# maior e menor valores
# Inicializa as variaveis com valores nulos
cont = media = soma = maior = menor = 0
opc = ''
while opc in 'S':  # o programa roda enquanto tiver 's' na opc
    num = int(input('Digite um número: '))
    opc = str(input('Quer continuar? [S/N]')).strip().upper()
    cont += 1  # conta quantas vezes o programa rodou
    soma += num  # a cada numero digitado ele soma aos anteriores
    media = soma/cont  # faz o calculo da media de todos os numeros digitados
    if cont == 1:  # Se so for digitado um número, esse número é o maior e o menor
        menor = maior = num
    else:  # se for digitado mais de um número
        if num > maior:  # se o num atual for maior que o anterior, o atual passa a ser o maior
            maior = num
        if num < menor:  # se o num atual for menor que o anterior, o atual passa a ser menor
            menor = num
print('''Você digitou {} números e a média entre eles foi {:.2f}!
E o maior valor foi de {} e o menor foi {}!'''.format(cont, media, maior, menor))
