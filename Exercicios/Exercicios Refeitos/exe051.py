cont = 0
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
for x in range(primeiro_termo, primeiro_termo+(10-1)*razao, razao):
    print(f'{x}', end=' -> ')
print('Acabou')