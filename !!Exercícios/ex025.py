# Verificador de silva no nome
nome = str(input('Digite seu nome: ')).strip().lower()
print('Seu nome tem Silva?', 'silva' in nome)

# jeito com if else
if 'silva' in nome:
    print('Seu nome tem Silva? Tem.')
else:
    print('Seu nome tem Silva? Não tem.')