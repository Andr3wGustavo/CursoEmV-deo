num = soma = 0  # Inicializa as variaveis
while True:  # roda "eternamente"
    num = int(input('Digite um número: '))
    if num == 999:  # se o número digitado for 999
        break  # interrompe o while
    soma += num
print(f'A soma dos números digitados é {soma}')
