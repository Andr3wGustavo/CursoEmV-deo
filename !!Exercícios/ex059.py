# Menu de opçoes matemáticas
from time import sleep
num = int(input('Digte o primeiro valor: '))
num1 = int(input('Digite o segundo valor: '))
maior = 1  # Inicializa a variavel pra n bugar o programa
opc = 1  # Inicializa a variavel pra n bugar o programa
while opc != 5:  # Enquanto a opção não for 5, o programa continua rodando
    print('-=' * 15)
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    opc = int(input('>>>> Qual é a sua opção? '))
    if opc == 1:  # se a opção for 1, ele executa a soma
        soma = num + num1
        print('A soma entre {} + {} é {}.'.format(num, num1, soma))
    elif opc == 2:  # se a opção for 2, ele executa a multiplicação
        multiplicar = num * num1
        print('O produto entre {} x {} é {}.'.format(num, num1, multiplicar))
    elif opc == 3:  # se a opção for 3, ele executa um algoritimo que mostra qual dos numeros é maior
        if num > num1:  # se o num for maior que num1, ele passa a ser o maior
            maior = num
            print('O maior número entre {} e {} é {}.'.format(num, num1, maior))
        elif num1 > num:  # se num1 for maior que num1, ele passa a ser o maior
            maior = num1
            print('O maior número entre {} e {} é {}.'.format(num, num1, maior))
        else:  # Verifica se num1 e num são iguais
            print('Não há valor maior, {} e {} são iguais!'.format(num, num1))
    elif opc == 4:  # se a opção for 4, o programa reseta os números
        print('Informe os números novamente!')
        num = int(input('Digte o primeiro valor: '))
        num1 = int(input('Digite o segundo valor: '))
    elif opc > 5 or opc < 1:  # se a opção for maior que 5 ou menor que 1, a opção é inválida
        print('Opção inválida, tente novamente!')
    sleep(2)
print('Finalizando...')
print('-=' * 15)
