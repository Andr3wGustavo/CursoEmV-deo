# Progressão aritimetica

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('Os primeiros termos da PA são:')
for c in range(primeiro_termo, primeiro_termo + razao * 10, razao):
    print(c, end='-')
print('FIM!')