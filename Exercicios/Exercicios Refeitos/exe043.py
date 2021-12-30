peso = float(input('Digite o peso da pessoa: '))
altura = float(input('Digite a altura da pessoa:' ))

if peso/(altura**2) < 18.5:
    print(f'Peso abaixo do normal!')
elif 18.5 < peso/(altura**2) < 25:
    print(f'Peso ideal!')
elif 25 < peso/(altura**2) < 30:
    print(f'Sobrepeso!')
elif 30 < peso / (altura ** 2) < 40:
    print(f'Obeso!')
else:
    print(f'Obesidade morbida!')