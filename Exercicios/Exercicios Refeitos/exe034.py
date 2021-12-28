salario = float(input('Digite o slaraio do funcionario: '))
if salario <= 1250:
    print(f'O salario do funcionario apos o aumento é de R${salario+(salario*0.15)}')
else:
    print(f'O salario do funcionario apos o aumento é de R${salario+(salario*0.1)}')