numeros = []
fatorial = []
i=0

for i in range(0,1000):
    print("Preencha o conjunto com 10 numeros {}" .format(i+1))
    num = int(input("Numero: "))
    if(num>=0):
        numeros.append(num)
    else:
        break
    


for i in range(0,len(numeros)):
    n = numeros[i]
    fat = 1
    x = 2

    while x <= n:
        fat = fat*x
        x = x + 1

    fatorial.append(fat)

print(fatorial)
