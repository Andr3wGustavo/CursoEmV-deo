nome = input('Qual é o seu nome?')
print('Muito prazer em conhecer você {:20}'.format(nome)) #Faz aparecer em 20 caracteres
print('Muito prazer em conhecer você {:>20}'.format(nome)) #Faz o alinhamento a direta em 20 espaços
print('Muito prazer em conhecer você {:<20}'.format(nome)) #Faz o alinhamento a esquerda com 20 espaços
print('Muito prazer em conhecer você {:^20}'.format(nome))#Faz ficar centralizado em 20 espaços
print('Muito prazer em conhecer você {:}'.format(nome)) #Coloca "=" entre a palavra centralizada
print('Muito prazer em conhecer você {:.3f}') #Coloca tres casas decimais flutuantes
#Coloca-se ,end ='', para não quebrar a linha
#Para quebrar o print, utiliza-se \n