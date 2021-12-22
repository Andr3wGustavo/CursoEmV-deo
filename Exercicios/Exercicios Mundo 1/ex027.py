# Verifica o primeiro e o ultimo nome de uma pessoa
nome = str(input('Digite seu nome: ')).strip().split()
print('Prazer em te conhecer!')
print('O seu primeiro nome é {}'.format((nome[0])))  # mostra a primeira posição do split
print('O seu último nome é {}'.format(nome[len(nome)-1]))  # mede o nome e pega a ultima posicão do split
