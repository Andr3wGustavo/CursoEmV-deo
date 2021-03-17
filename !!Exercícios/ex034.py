# Aumento de salário
salario = float(input('Digite o valor do salário atual:'))
maior_aumento = (salario*15)/100 + salario
menor_aumento = (salario*10)/100 + salario
if salario >= 1250:  # Se o salario for mais de 1250, ele recebe o menor aumento, apenas de 10%
    print('Seu novo salário será de R${:.2f}'.format(menor_aumento))
else:  # Se o salario for menos de 1250, ele recebe o aumento de 15%
    print('Seu novo salário será de R${:.2f}'.format(maior_aumento))

