# Verificador de nome de cidade
# Jeito usando if else
nome_cidade = str(input('Digite o nome da cidade: ')).strip().upper()
if 'SANTO' in nome_cidade:
    print('True')
else:
    print('False')

# Jeito simples
print(nome_cidade[:5].upper() == 'SANTO')
