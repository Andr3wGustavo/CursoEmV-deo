num = int(input('Digite um número: '))
for c in range(1, num + 1):  # Começa do 1 e conta até o num escolhido
   print(c)
print('Fim')

inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))

for c1 in range(inicio, fim + 1, passo):  # Ele vai do inicio digitado até o fim, saltando em passos
    print(c1)

s = 0
for c2 in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('A soma de todos os valores digitados é igual a {}'.format(s))  # Último valor digitado

