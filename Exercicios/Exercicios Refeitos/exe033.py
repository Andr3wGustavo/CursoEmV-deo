num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite mais um numero: '))

if num1>num2>num3: print(f'O numero maior entre {num1}, {num2} e {num3} é: {num1}')

elif num2>num1>num3: print(f'O numero maior entre {num1}, {num2} e {num3} é: {num2}')

else:
    print(f'O numero maior entre {num1}, {num2} e {num3} é: {num3}')