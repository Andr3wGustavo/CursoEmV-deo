from datetime import date
ano = int(input('Digite um ano, digite 0 para o ano atual:'))
if ano == 0:
    ano = date.today().year  # Pega o ano atual da maquína
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    # O comando acima, verifica se o ano é divisivel por 4
    # e se ele não é divisivel por 100, pra se encaixar nos criterios de ano bissexto
    # mas se o ano for divisivel por 400, ele conta como bissexto, se encaixando em outro critério
    print('{} é um ano BISSEXTO!'.format(ano))
else:
    print('{} NÃO é BISSEXTO'.format(ano))
