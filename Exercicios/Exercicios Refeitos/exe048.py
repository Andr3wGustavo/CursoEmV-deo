soma = 0
cont = 0
for x in range(1, 501):
    if x % 3 == 0 and x % 2 != 0:
        soma += x #se estiver dentro das condicoes ele adiciona a soma
        cont += 1 #conta cada vez q a condição foi satisfeita
print(soma)