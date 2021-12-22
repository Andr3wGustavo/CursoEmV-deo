# Validação de dados, método do guanabara

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]  # elimina espaços, pega a primeira letra maiuscula
while sexo not in 'FM':  # Enquanto não tiver 'F' ou 'M' em sexo ele considera invalido
    sexo = str(input('Dados inválidos, Tente Novamente: '))
print('Sexo {} registrado com sucesso!'.format(sexo))
