preco_produto = float(input('Digite o valor do produto: '))
condicao = int(input('\nEscolha como deseja pagar! \n'
                     '\n - DINHEIRO/CHEQUE [1]\n'
                     ' - CARTÃO DE CRÉDITO [2]\n'
                     ' - 2x CARTÃO DE CRÉDITO [3]\n'
                     ' - 3x ou Mais CARTÃO DE CRÉDITO [4]\n'
                     '\nDigite uma das opçoes: '))

if condicao == 1:
    print(f'O produto custará R${preco_produto-(preco_produto*0.10)}')
elif condicao == 2:
    print(f'O produto custará R${preco_produto - (preco_produto * 0.05)}')
elif condicao == 3:
    print(f'O produto custará R${preco_produto}')
elif condicao == 4:
    print(f'O produto custará R${preco_produto + (preco_produto*0.2)}')