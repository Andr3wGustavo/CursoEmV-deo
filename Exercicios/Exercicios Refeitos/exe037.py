x = int(input('Digite um numero inteiro para converter: '))
escolha = int(input(' [1] Binario\n'
                    ' [2] Octal\n'
                    ' [3] Hexadecimal\n'
                    'Digite para qual base deseja converter:  '))
if escolha==1:
    print(f'Esse numero em binario é {bin(x)[2:]}')
elif escolha==2:
    print(f'Esse numero em octal é {oct(x)[2:]}')
elif escolha==3:
    print(f'Esse numero em hexadecimal é {hex(x)[2:]}')