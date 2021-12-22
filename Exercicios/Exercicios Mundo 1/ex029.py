# Leitor de velocidade
velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade - 80)*7  # Pega a diferença entre o limite e a velocidade
if velocidade >= 80:  # Se a velocidade passar de 80, o carro será multado
    print('''Multado, voce excedeu o limite de velocidade de 80km/h
    Você deve pagar uma multa de R${:.2f}!'''.format(multa))

print('Tenha um bom dia! Dirija com segurança!')
