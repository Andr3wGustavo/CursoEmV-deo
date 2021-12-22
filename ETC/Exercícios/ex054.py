# Leitor de maioridade
from datetime import date
ano_atual = date.today().year  # Usa o ano atual do computador
maior_idade = 0  # Inicializa a variavel com o valor 0
menor_idade = 0  # Inicializa a variavel com o valor 0
for c in range(1, 8):  # repete cada comando 7x
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = ano_atual - nascimento  # Faz o calculo da idade
    if idade >= 21:  # Se a idade for maior que 21, 1 valor é somando ao total de maiores de idade
        maior_idade += 1
    else:  # Se a idade não for maior que 21, 1 valor é adicionado ao total de menores de idade
        menor_idade += 1
print('Há um total de {} pessoas maiores de idade!'.format(maior_idade))
print('Há um total de {} pessoas menores de idade!'.format(menor_idade))





