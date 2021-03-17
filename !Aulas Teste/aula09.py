# Fatiamento de uma string
frase = 'Curso em Video'
print(frase[3])  # Fatia a string do 0 ao 3
print(frase[4:11])  # Fatia do 4 ao 10, pois o 11 não conta
print(frase[:4])  # Fatia do começo da string até o caracter 3
print(frase[2:])  # Fatia do caracter 2 e vai até o fimd da string
print(frase[1:13:2])  # Fatia do 1 ao 12, pulando de 2 em 2
print(frase[2::3])  # Fatia do caracter 2 e vai até o fim, pulando de 3 em 3

# Análise de uma string
print(frase.count('O'))  # Conta quantos vezes aparece a letra 'O'
print(frase.count('O', 0, 13))  # Conta quantos 'O' tem do 0 ao 12
print(len(frase))  # Conta quantos caracteres tem a frase
print(len(frase.strip()))  # Mostra o tamanho da frase, depois de remover os espaços
print(frase[0])  # Mostra a primeira letra da string
print('Curso' in frase)  # Mostra se dentro da string tem a palavra 'Curso'
print(frase.find('Curso'))  # Mostra quantas vezes encontra 'Curso' na string, e onde começa

# Transformação de um string
print(frase.replace('Video', 'Android'))  # Subsitui a palavra 'Video' por 'Android'
print(frase.upper())  # Coloca a frase em Maiusculo
print(frase.lower())  # Coloca a frase em minusculo
print(frase.capitalize())  # Joga todos os caracteres e apenas a primeira letra fica maisculo
print(frase.title())  # Analisa quantas palavras tem na string, coloca o inicio maiusculo em todas
print(frase.strip())  # Remove todos os espaços inuteis da string
print(frase.rstrip())  # Remove os espaços inuteis do aldo direito
print(frase.lstrip())  # Remove os espaços do lado esquerdo
print(frase.lower().find('Curso'))

# Divisão de uma string
print(frase.split())  # Ele divide a string, considerando os espaços, ele divide cada palavra, e numera elas e uma lista
print('-'.join(frase))  # Esse comando junta as strings, utilizando '-'
dividido = frase.split()
print(dividido[0])  # Mostra a primeira palavra depois de dividir a string
print(dividido[2])  # Mostra a terceira palavra depois de dividir a string
print(dividido[2][3])  # Mostra a terceira depois de dividir e mostra o caracter 3
