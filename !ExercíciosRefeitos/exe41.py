# Leitor de categoria de um atleta
from datetime import date
birth = int(input('Type your birth year: '))
yo = date.today().year - birth
if yo <= 9:
    print('The athlete is {} years old, and fits in the category MIRIM!'.format(yo))
elif 9 < yo <= 14:
    print('The athlete is {} years old, and falls into the CHILD category!'.format(yo))
elif 14 < yo <= 19:
    print('The athlete is {} years old, and falls into the JUNIOR category!'.format(yo))
elif 19 < yo <= 25:
    print('The athlete is {} years old, and fits in the SENIOR category!'.format(yo))
elif yo > 25:
    print('The athlete is {} years old, and falls into the MASTER category!'.format(yo))
