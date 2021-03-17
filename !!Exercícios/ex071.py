# Banco do André
print('=' * 30)
print('{:^30}'.format('BANCO DO ANDRÉ'))
print('=' * 30)
sacar = int(input('Quanto deseja sacar? '))
totalcedulas = 0  # contador de celulas sacadas
cedula = 50  # inicializa o valor da cedula como a maior dipsonivel, no caso 50
total = sacar
while True:  # roda o programa 'infinitamente'
    if total >= cedula:  # se o valor total a ser sacado for maior ou igual a 50
        total -= cedula  # retira-se 50 do caixa
        totalcedulas += 1  # adiciona mais 1 na soma do contador
    else:  # se o total a ser sacado for menor que 50
        if totalcedulas > 0:  # só mostra o print das notas que forem sacadas
            print(f'Total de {totalcedulas} cédulas de R${cedula}' )
        if cedula == 50:  # se a cedula ainda for  igual a 50 mesmo o valor sendo menor que 50
            cedula = 20  # a cedula passa a ser 20
        elif cedula == 20:  # se a cedula ainda for 20 mesmo o valor sendo menor que 20
            cedula = 10  # a cedula passa a ser 10
        elif cedula == 10:  # se a cedula aidna for 10 mesmo o valor sendo menor que 10
            cedula = 1  # a cedula passa a ser 1
        totalcedulas = 0  # reinicializa a contagem de cedulas distribuidas para cada cedula diferente
        if total == 0:  # se finalmente o total a sacar for 0, o programa para de rodar
            break
print('=' * 30)