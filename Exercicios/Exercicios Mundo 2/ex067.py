# Tabuada 3.0
while True:  # Roda o codigo infinitamente
    print('-'*35)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    if num < 0:  # se o numero digitado for menor que 0, ou seja, negativo, ele para  de rodar
        break  # quebra o loop
    for c in range(1, 11):  # repete o print abaixo 10x
        print(f'{num} x {c} = {num*c}')

