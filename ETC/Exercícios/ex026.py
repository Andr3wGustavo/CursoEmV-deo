# Analisador de frases
frase = str(input('Digite um frase: ')).strip().upper()
quantos_a = frase.count('A')  # Conta quantos 'A' tem na string
primeira_letra_A = frase.find('A')+1  # Começa procurando do começo da string
ultima_letra_A = frase.rfind('A')+1  # Começa procurando do final da string
print('A letra A aparece {} na frase.'.format(quantos_a))
print('A primeira letra A começa na posição {}'.format(primeira_letra_A))
print('A última letra A aparece na posição {} '.format(ultima_letra_A))
