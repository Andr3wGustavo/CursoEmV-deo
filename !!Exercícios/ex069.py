# Cadastrando uma pessoa
maiores_idade = 0  # Inicializa a variavel com um valor nulo
homens = 0
mulheres = 0
sexo = ''
continuar = 'S'  # Inicializa a variavel continuar como 'S'
while continuar != 'N':  # O programa roda até o usario querer parar
    print('-' * 25)
    print('  CADASTRE UMA PESSOA  ')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if sexo == 'M' or sexo == 'F':  # Só roda se sexo for 'M' ou 'F'
        print('-' * 25)
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        if continuar == 'S' or continuar == 'N':  # Só roda se ele digitar uma opção válida
            if idade >= 18:  # Se a idade fir maior que 18, ele soma mais um na contador de maiores
                maiores_idade += 1
            if sexo == 'M':  # Se o sexo for 'M', ele soma mais um no contador de homens
                homens += 1
            if idade < 20 and sexo == 'F':  # Se a idade for menor que 20, e o sexo for feminino
                mulheres += 1  # Soma mais um na variavel mulheres
        else:  # Se o usuário não digitar uma opção válida
            print('Você digitou um comando inválido, tente novamente!')
    else:  # Se o usuário não digitar uma opção válida
        print('Você digitou um comando inválido, tente novamente!')
print('Total de pessoas com mais de 18 anos: {}'.format(maiores_idade))
print('Ao todo temos {} homen(s) cadastrado(s)!'.format(homens))
print('E temos {} mulhere(s) com menos de 20 anos'.format(mulheres))
