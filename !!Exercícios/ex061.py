# Progressão aritimetica 3.0
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 0
while contador <= 10:  # o programa repete 10x
    print('{}'.format(primeiro_termo), end=' ➔ ')
    contador += 1  # A cada vez que ele executa o codigo, soma-se mais uma vez que ele ja rodou
    primeiro_termo += razao  # A cada codigo rodado, o primeiro termo passa ser ele mais a razao
print('Fim')

