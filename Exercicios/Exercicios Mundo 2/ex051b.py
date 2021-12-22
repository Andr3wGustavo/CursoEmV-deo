# Forma mais facil de resolver o ex51
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo_termo = primeiro_termo + (10 - 1)*razao
for x in range(primeiro_termo, decimo_termo + 1, razao):
    print('{}'.format(x), end='-')
print('FIM')