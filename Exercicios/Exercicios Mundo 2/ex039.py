# Verificador de alistamento
from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
alistamento = nascimento + 18

if alistamento == ano_atual:  # Indica se o ano de alistamento é o ano atual
    print('Você tem {} anos em {} e deve se alistar esse ano!'.format(idade, ano_atual))
elif alistamento > ano_atual:  # Indica quando voce deve se alistar
    print('Você tem {} anos e deve se alistar somente em {}'.format(idade, alistamento))
elif alistamento < ano_atual:  # Indica quando voce devia ter se alistado
    print('Você tem {} anos e deveria ter se alistado em {}'.format(idade, alistamento))
