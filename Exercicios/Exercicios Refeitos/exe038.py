x = int(input('Digite o primero valor: '))
y = int(input('Digite o segundo valor: '))
if x>y:
    maior = x
    print(f'Entre {x} e {y} o maior valor é {x}')
elif y>x:
    maior = y
    print(f'Entre {x} e {y} o maior valor é {y}')
else:
    print(f'Os dois valores são iguais!')