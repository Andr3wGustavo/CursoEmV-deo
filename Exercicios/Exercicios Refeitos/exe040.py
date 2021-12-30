nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

if (nota1+nota2)/2 <= 5.0:
    print(f'O aluno tirou {(nota1+nota2)/2} de media e esta de REPROVADO!')
elif 5.0 < (nota1+nota2)/2 <= 6.9:
    print(f'O aluno tirou {(nota1+nota2)/2} de media e esta de RECUPERAÇÃO!')
else:
    print(f'O aluno tirou {(nota1+nota2)/2} de media e esta de APROVADO!')
