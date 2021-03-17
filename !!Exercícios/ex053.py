# Analisador de palíndromo
frase = str(input('Digite uma frase: ')).strip().upper()  # lê a frase, coloca para maisuculo, e tira os espaços
divido = frase.split()  # Divide a frase em palavras
junto = ''.join(divido)  # Junta as palavras que foram divididas
inverso = ''
for a in range(len(junto) - 1, -1, -1):  # Vai da ultima letra até a primeira, de tras pra frente
    inverso += junto[a]  # acumula cada letra da frase dependendo do tamanho dela
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:  # Se o inverso da frase for igual a frase, é palindromo, senão não é
    print('A frase digitada é PALÍNDROMO!')
else:
    print('A frase digitada NÃO É PALÍNDROMO!')

