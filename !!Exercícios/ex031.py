# Calculadora de viagens
distancia =float(input('Digite a distância percorrida: '))
viagem_longa = distancia*0.45
viagem_curta = distancia*0.50
if distancia >= 200:
    print('O preço da viagem foi de R${:.2f}'.format(viagem_longa))
else:
    print('O preço da viagem foi de R${:.2f}'.format(viagem_curta))
