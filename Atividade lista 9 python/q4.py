lista = []
i=0


for i in range(0,20):
    print("Insira nome e salario {}" .format(i+1))
    nome = input("Nome: ")
    oldS = int(input("salario: "))
    

    reaj = (oldS * 8) / 100
    salario = oldS + reaj
        
    trab = [nome, salario] 
    

    lista.append(trab)

print(lista)
