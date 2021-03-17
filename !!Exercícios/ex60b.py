# fatorial
num = int(input('Digte um número: '))
fatorial = 1  # Inicializa a variavel com um valor nulo de multiplicação
while num > 0:  # Enquanto o numero for maior que 0 ele excuta, pois multplicar por 0 estraga o fatorial
    print('{}'.format(num), end='')
    if num > 1:  # Se o num for maior que 1 ele coloca 'x', se não coloca '='
        print(' x ', end='')
    else:
        print(' = ', end='')
    fatorial *= num  # Cada vez que ele roda o codigo, multiplica o numero anterior pelo num - 1
    num -= 1  # Faz a função de cada vez que o codigo rodar, subtrair 1 do num
print(fatorial)
