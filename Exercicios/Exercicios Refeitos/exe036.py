valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario do comprador: '))
anos = int(input('Digite em quantos anos a casa sera paga: '))
if (valor/anos*12) > (salario*0.3):
    print('O emprestimo foi NEGADO, pois o valor EXCEDE 30% do salario!')
else:
    print('O emprestimo foi APROVADO!')