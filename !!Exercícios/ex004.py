n = input('Digite algo: ')
print('O tipo primtivo desee valor é:{}'.format(type(n)))
print('Só tem espaços? {}'.format(n.isspace()))
print('É um número? {}'.format(n.isnumeric()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('Esta em maiúsucla? {}'.format(n.isupper()))
print('Esta em minúscula? {}'.format(n.islower()))
print('Esta capitalizada? {}'.format(n.istitle()))

