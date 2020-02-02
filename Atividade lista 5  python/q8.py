aluno = input('nome do aluno: ')
nota1 = int(input('nota 1: '))
nota2 = int(input('nota 2: '))

media = (nota1 + nota2) /2

if media >= 7:
    print(aluno, 'aprovado')
if media < 7:
    print(aluno, 'reprovado')
