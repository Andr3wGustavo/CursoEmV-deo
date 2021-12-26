from datetime import date
from time import sleep

year = int(input('Digite um ano e lhe mostrarei se é BISSEXTO ou\nDigite 0 para analisar o ano atual: '))
sleep(1)
if year == 0:
  year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print('É BISSEXTO')
else:
  print('NÃO É BISSEXTO')
