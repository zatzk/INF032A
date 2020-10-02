lista = []
i=0


for i in range(0,15):
    print("Insira nome e notas do aluno {}" .format(i+1))
    nome = input("Nome: ")
    n1 = int(input("nota 1: "))
    n2 = int(input("nota 2: "))

    media = (n1+n2) / 2
    if media >= 5:
        condicional = 'AP'
    else:
        condicional = 'RP'
        
    alunos = [nome,n1, n2, media, condicional] 
    

    lista.append(alunos)

print(lista)
