nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota2 + nota1)/2
print('A sua média foi {:.1f}'.format(media))
if media >= 6.0:  # Se a média for maior que 6, ele da parabens
    print('Sua média foi boa, parabéns!')
else:  # Se a média for menor que 6, ele fala pra estudar mais
    print('Sua média foi ruim, estude mais!')




