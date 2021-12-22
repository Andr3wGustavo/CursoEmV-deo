# Leitor de peso
mais_leve = 0  # Inicializa a variavel com o valor 0
mais_pesada = 0  # Inicializa a variavel com o valor 0
for p in range(1, 6):  # Repeter os comandos 5x
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if peso == 1:  # Se só tiver lido uma opção, o maior e menor pesos, passam a ser o proprio primeiro
        mais_pesada = peso
        mais_leve = peso
    else:
        if peso > mais_pesada:  # Se o ultimo peso lido for maior que o o maior peso, ele passa a ser o mais pesado
            mais_pesada = peso
        if peso < mais_pesada:  # Se o ultimo peso lido for menor que o menor peso, ele passa a ser o menor peso
            mais_leve = peso
print('O mais pessado é {}'.format(mais_pesada))
print('O mais leve é {}'.format(mais_leve))

