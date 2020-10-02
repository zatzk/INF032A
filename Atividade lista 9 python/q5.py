lista = []
i=0


for i in range(0,5):
    print("Insira nome e idade {}" .format(i+1))
    strnome = input("Nome: ")
    idade = int(input("idade: "))
    nome = strnome.lower()
    
    first_char = nome[0]
    

    if first_char == 'l':
        pessoas = [nome, idade]
    if first_char == 'm':
        pessoas = [nome, idade]
    if first_char == 'n':
        pessoas = [nome, idade]
    if first_char == 'o':
        pessoas = [nome, idade]
    if first_char == 'p':
        pessoas = [nome, idade]
    if first_char == 'q':
        pessoas = [nome, idade]
    if first_char == 'r':
        pessoas = [nome, idade]
    if first_char == 's':
        pessoas = [nome, idade]

    lista.append(pessoas)
        

print(lista)
