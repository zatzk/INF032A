conjunto1 = []
conjunto2 = []
comum = []
i=0
x=0
for i in range(0,10):
    print("Preencha o conjunto com 10 numeros {}" .format(i+1))
    
    num1 = int(input("Numero: "))
    conjunto1.append(num1)
    
for x in range(0,20):
    print("Preencha o conjunto com 20 numeros {}" .format(x+1))
    
    num2 = int(input("Numero: "))
    conjunto2.append(num2)

comum=set(conjunto1).intersection(conjunto2)

print("\n Numeros em ambas as listas:",comum)
