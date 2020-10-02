numeros = []
count=0
for i in range(0,20):
    print("Preencha o conjunto com 20 numeros {}" .format(i+1))
    num = int(input("Numero: "))
    numeros.append(num)

for i in range(0,20):
    if (numeros[i]%2 == 0):
        count+=1
media = sum(numeros)/len(numeros)

print("maior elemento:", max(numeros))
print("menor elemento:", min(numeros))
print("total de elementos pares:", count)
print("media dos elementos:", media)
