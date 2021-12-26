speed = float(input('Digite a velocidade do carro: '))
if speed>80:
    print(f'Voce foi multado! O custo será de {(speed-80)*7}')
else:
    print(f'Voce esta dentro do limite de velocidade, parabens!')