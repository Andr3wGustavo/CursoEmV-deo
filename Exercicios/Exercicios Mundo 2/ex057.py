# Leitor de sexo, tem alguns erros

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo != 'F' and sexo != 'M':  # Enquanto não tiver 'F'e 'M' no sexo ele continua rodando
    print('{}Digite uma reposta válida!{}'.format('\033[31m', '\033[m'))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))
