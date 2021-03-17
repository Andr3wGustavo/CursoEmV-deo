#calculadora de aluguel de um carro
dias = int(input('Digite quantos dias o carro foi alugado:'))
percorrido = float(input('Digite quantos Km foram rodados:'))
precototal = (60*dias) + (percorrido*0.15)
print('O preço total a ser pago pelo aluguel será de {:.2f}R$'.format(precototal))

