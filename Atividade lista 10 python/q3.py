numeros = []
inverso = []
i=0

for i in range(0,10):
    print("Preencha o conjunto com 10 numeros {}" .format(i+1))
    num = int(input("Numero: "))
    if(num>0):
        numeros.append(num)
    else:
        break

for i in range(0,10):
    
    soma = numeros[i]*2
    
    inv = numeros[i] - soma

    inverso.append(inv)

print(inverso)
