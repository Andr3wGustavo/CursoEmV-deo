# Condição de pagamento
valor = float(input('Digite o valor do produto: '))
pagamento = int(input('''[1] Avista dinheiro/cheque\n[2] Avista no cartão
[3] Em até 2x no cartão\n[4] 3x ou mais no cartão\nEscolha um condição de pagamento: '''))

if pagamento == 1:
    desconto = valor - (valor * 10 / 100)
    print('Você terá 10% de desconto! O valor do produto será R${:.2f}'.format(desconto))
elif pagamento == 2:
    desconto = valor - (valor * 5 / 100)
    print('Você terá 5% de desconto!O valor do produto será R${:.2f}'.format(desconto))
elif pagamento == 3:
    print('O valor do seu produto será R${:.2f} e será parcelada em 2x de R${.:2f}'.format(valor, valor/2))
elif pagamento == 4:
    juros = valor + (valor * 20 / 100)
    parcelas = int(input('Em quantas parcelas deseja pagar? '))
    if parcelas <= 10:
        print('Você pagará 20% de juros! O valor do seu produto será de R${:.2f}, feitos {}x de R${:.2f} no cartão\n'
              ''.format(juros, parcelas, juros / parcelas))
    else:
        print('O limite da loja é de 10x no cartão!')
else:
    print('Você digitou uma opção invalida, tente novamente!')
