distance = float(input('Digite a distancia da viagem: '))
if distance<=200:
    print(f'O custo da viagem foi de R${0.50*distance}')
else:
    print(f'O custo da viagem foi de R${0.45 * distance}')