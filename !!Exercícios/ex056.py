# Verificador de pessoa

# Essas variaveis abaixo criam um valor incial para elas serem manipuladas depois
soma_idades = 0
nome_do_veio = ''
homem_mais_velho = 0
idade_mulheres = 0

for c in range(1, 5):  # Cria 4x cada input abaixo, ou seja uma pergunta pra cada pessoa
    print('----- {}ªPESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()  # Joga a string pra maisculas, facilitando no if posteriormente
    soma_idades += idade  # A cada input em 'idade' o valor se soma a 'soma_idades'

    if 'M' in sexo and c == 1:  # Verifica se é homem e estabelece o primeiro input de um homem, como sendo mais velho
        homem_mais_velho = idade
        nome_do_veio = nome

    if 'M' in sexo and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_do_veio = nome_do_veio
        '''Verifica se é homem, mas se a idade for maior do que o  ultimo homem inserido
        o homem mais velho entre eles, passa a ser o mais velho para o algoritimo'''

    if 'F' in sexo and idade < 20:  # Verifica se há alguma mulher que tem menos de 20 anos, se tiver ele add na lista
        idade_mulheres += 1

media_idades = soma_idades/4  # Calcula a media de todas as idades inseridas
print('A média de idade do grupo é de {} anos!'.format(media_idades))
print('O homem mais velho tem {} anos e se chama {}!'.format(homem_mais_velho, nome_do_veio))
print('Ao todo são {} mulheres com menos de 20 anos!'.format(idade_mulheres))
