# Soma de numeros pares
print('Digite 6 numeros no terminal! ')
soma = 0
contador = 0
for x in range(1, 7):
    num = int(input('Digite o {}º numero: '.format(x)))

    if num % 2 == 0:  # Se for par ele faz a soma
        soma += num  # Acumulador, a cada número par, ele soma
        contador += 1  # Conta quantos números pares foram digitados
print('A soma entre os {} numeros pares  digitados  e {}.'.format(contador, soma))
