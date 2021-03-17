# Varios números com flag
soma = contador = 0  # incializa as variaveis
while True:  # roda infinitamente
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break  # quebra o while se digitar 999
    soma += num  # soma cada número adcionado
    contador += 1  # conta quantas vezes o programa rodou
print(f'A soma dos {contador} números digitados é {soma}!')
