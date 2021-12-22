#calculadora de desconto
preco = float(input('Digite o preço do produto:'))
precofinal = preco - ((preco*5)/100)
print('O preço final do produto será {:.2f}R$'.format(precofinal))

