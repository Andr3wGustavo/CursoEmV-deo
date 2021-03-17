# Aprovação de emprestimo bancario
valor_da_casa = float(input('Digite o valor da casa: '))
valor_do_salario = float(input('Digite o valor do salário: '))
quantos_anos = int(input('Digite em quantos anos será pago: '))
parcela = valor_da_casa/(quantos_anos*12)
if parcela <= valor_do_salario*30/100:  # Se o valor da parcela for menor que 30% do salario, aprova o emprestimo
    print('O empréstimo foi APROVADO!\nO valor da parcela será de R${:.2f} por mês.'.format(parcela))
else:
    print('O empréstimo foi NEGADO! O valor da parcela seria de R${:.2f}'.format(parcela))
print('Obrigado pela preferência,Volte sempre!')
