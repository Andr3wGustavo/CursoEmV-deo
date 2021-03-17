# Exercicio 61 melhorado
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 0  # Inicializa a variavel com valor nulo
total = 0   # Inicializa a variavel com valor nulo
amais = 10   # Inicializa a variavel com valor do ultimo termo mostrado
while amais != 0:  # Enquanto o usuario não digitar 0, o programa continua rodando
    total += amais  # atribui quantas vezes o programa tem que rodar
    while contador <= total:  # enquanto o programa estiver rodando menos vezes que o total, ele continua rodando
        print('{}'.format(primeiro_termo), end=' ➔ ')
        contador += 1  # A cada vez que ele executa o codigo, soma-se mais uma vez que ele ja rodou
        primeiro_termo += razao  # A cada codigo rodado, o primeiro termo passa ser ele mais a razao
    print('Pausa')
    amais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados!'.format(total))


