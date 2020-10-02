numeros = []
fatorial = []
i=0

for i in range(0,10):
    print("Preencha o conjunto com 10 numeros {}" .format(i+1))
    num = int(input("Numero: "))
    numeros.append(num)



for i in range(0,10):
    n = numeros[i]
    fat = 1
    x = 2

    while x <= n:
        fat = fat*x
        x = x + 1

    fatorial.append(fat)

print(fatorial)

