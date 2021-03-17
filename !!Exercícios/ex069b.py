
maiores_idade = homens = mulheres = 0  # inicializa as variaveis utilizadas
print('-=' * 15)
print('CADASTRE UMA PESSOA')
print('-=' * 15)
while True:  # Roda o codigo infinito
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    print('-=' * 15)
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    print('-=' * 15)
    if sexo == 'M' or sexo == 'F' and opcao == 'N' or opcao == 'S':  # so roda se os comandos forem validos
        if idade >= 18:  # se a idade for menor ou igual a 18, soma mais 1 para o maiores de idade
            maiores_idade += 1
        if sexo == 'M':  # se o sexo for masculino, soma mais 1 na lista de homens
            homens += 1
        if sexo == 'F' and idade < 20:  # se a idade for feminino e menor que 20, adiciona a lista
            mulheres += 1
        if opcao == 'N':  # se a opção for sair 'N' o programa para de rodar
            break
    else:  # se algum comando for digitado errado ele reinicia
        print('Comandos inválidos, tente novamente!')
        print('-=' * 15)
print(f'Total de pessoas com mais de 18 anos: {maiores_idade}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20  .')