from datetime import date

nasc = int(input('Digite em que ano voce nasceu: '))

if date.today().year - nasc <= 17:
    print(f'Voce ainda não esta na idade de se alistar! Ainda faltam {-(date.today().year - nasc - 18)} '
          f'anos para voce se alistar')
elif date.today().year - nasc == 18:
    print(f'Voce ja esta na idade de se alistar!')
elif date.today().year - nasc > 18:
    print(f'Voce ja passou da idade de se alistar! Voce esta atrasado em {date.today().year - nasc - 18} anos!')
