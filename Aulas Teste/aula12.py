# Condições aninhadas
nome = str(input('Digite seu nome: '))
if nome == 'André':
    print('Que nome bonito!')
elif nome == 'Julia' or nome == 'Ana' or nome == 'Bruna':
    print('Que nome lindo moça!')
elif nome in 'Pedro Mateus Jorge':  # elif é um condição aninhada, ele esta dentro de if, ele da mais opçoes
    print('Seu nome é bem comum no Brasil.')
else:
    print('Seu nome é sem graça!')
print('Tenha um bom dia, {}!'.format(nome))
