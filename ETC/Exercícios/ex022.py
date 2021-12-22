# Programa que le nome das piazada

nome = str(input('Digite seu nome: ')).strip().title()
maiusculo = nome.upper()
minusculo = nome.lower()
dividido = nome.split()  # Divide o nome em partes
quantas_letras = len(''.join(dividido))  # Junta as partes do nome e conta sem espaços
primeiro_nome = len(dividido[0])  # Conta quantas letras tem o primeiro nome
print('O nome em maiusculo é: {}'.format(maiusculo))
print('O nome em minusculo é: {}'.format(minusculo))
print('O nome completo tem {} letras'.format(quantas_letras))
print('O primeiro nome é {} e tem {} letras'.format(dividido[0].title(), primeiro_nome))
