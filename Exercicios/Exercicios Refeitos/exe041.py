from datetime import date

nasc = int(input('Digite o ano de nascimento do atleta: '))

if date.today().year - nasc <= 9:
    print(f'Categoria: CRIANÇA')
elif 9 < date.today().year - nasc <= 14:
    print(f'Categoria: INFANTIL')
elif 14 < date.today().year - nasc <= 19:
    print(f'Categoria: JUNIOR')
elif 19 < date.today().year - nasc <= 25:
    print(f'Categoria: SÊNIOR')
else:
    print(f'Categoria: MESTRE')