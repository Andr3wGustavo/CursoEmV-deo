# Mostrador de unidade, dezena, centena e milhar, utilizando manipulação de string
num = str(input('Ditgite um número de 0 a 9999: '))
dividido = ' '.join(num).split(num)  # Divide cada número em espaços e depois divide
print('Unidade:{}'.format(num[3]))
print('Dezena:{}'.format(num[2]))
print('Centena:{}'.format(num[1]))
print('Milhar:{}'.format(num[0]))
