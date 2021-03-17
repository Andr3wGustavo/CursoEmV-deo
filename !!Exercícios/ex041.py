# Leitor de categoria de um atleta
from datetime import date
ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano_nascimento
if idade <= 9:
    print('O atleta tem {} anos, e se encaixa na categoria MIRIM!'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos, e se encaixa na categoria INFANTIL!'.format(idade))
elif 14 < idade <= 19:
    print('O atleta tem {} anos, e se encaixa na categoria JUNIOR!'.format(idade))
elif 19 < idade <= 25:
    print('O atleta tem {} anos, e se encaixa na categoria SÊNIOR!'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos, e se encaixa na categoria MASTER!'.format(idade))
