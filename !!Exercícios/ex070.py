# Loja do andré
total = mais_de_mil = mais_barato = cont = 0  # inicializa as variaveis
nomeMB = ''
print('-' * 40)
print('{:-^40}'.format('LOJA SUPER BARATÃO'))
print('-' * 40)
while True:  # roda o codigo infinitamente
    nome_produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$ '))
    cont += 1  # conta quantas vezes o codigo roda
    total += preco  # a cada vez que o preco é digitado ele acumula(soma) os valores anteriores
    if preco >= 1000:  # se o preço for maior que 1000, ele adiciona mais 1 na lista
        mais_de_mil += 1
    if cont == 1 or preco < mais_barato:
        # se só houver 1 preco digitado, entao ele é o mais barato, se não ele ve qual é o mais barato
        mais_barato = preco
        nomeMB = nome_produto
    opcao = ''
    while opcao not in 'SN':  # enquanto o usuario não digitar um comando valido, fica rodando
        opcao = str(input('Quer continuar [S/N]: '))
    if opcao == 'N':  # se o usuario digitar 'N' o programa para de rodar
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais_de_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMB} custando R${mais_barato}')
