# Soma de todos os números impares que são multiplos de 3 e estão entre 1 e 500
soma = 0
contador = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:  # Se for multiplo de 3 e impar  ele soma
        soma += c  # Acumulador, ele vai acumulando os valores encontrados na condição
        contador += 1  # Soma 1 cada vez q a condição for verdadeiraa
print('A soma de todos os {} números divisiveis por 3, no intervalo de 1 a 500 é igual a {}.'.format(contador, soma))
