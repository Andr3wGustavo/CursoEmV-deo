# Calculadora de IMC
peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / altura ** 2

if imc < 18.5:
    print('Seu imc é {:.1f} e você esta ABAIXO do peso!'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu imc é {:.1f} e você esta no peso IDEAl!'.format(imc))
elif 25 <= imc < 30:
    print('Seu imc é {:.1f} e você esta com SOBREPESO!'.format(imc))
elif 30 <= imc < 40:
    print('Seu imc é {:.1f} e você esta com OBESIDADE!'.format(imc))
elif imc > 40:
    print('Seu imc é {:.1f} e você esta com OBSIDADE MÓRBIDA!'.format(imc))
