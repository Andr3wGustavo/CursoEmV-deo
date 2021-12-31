num1 = 0
soma = 0
cont = 0
for x in range(1,7):
    num1 = int(input('Digite um numero: '))
    if num1 % 2 == 0:
        soma += num1
        cont += 1
print(f'Dos 6 valores digitados, {cont} são pares, e a soma deles é {soma}!')



