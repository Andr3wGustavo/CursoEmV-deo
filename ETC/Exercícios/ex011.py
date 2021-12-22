#quantidade de tinta necessaria
altura = float(input('Digite a altura da parede:'))
largura = float(input('Digite a largura da parede:'))
area = largura*altura
litrosdetinta = area/2
print('Será necessário {:.2f} litros de tinta, para pintar a parede!'.format(litrosdetinta))
