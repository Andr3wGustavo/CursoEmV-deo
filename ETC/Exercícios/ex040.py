# Leitor de notas 2.0
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('Sua média foi de {:.1f}'.format(media))
if media < 5:
    print('REPROVADO!')
elif 7 > media >= 5:
    print('RECUPERAÇÃO!')
elif media >= 7:
    print('APROVADO!')

