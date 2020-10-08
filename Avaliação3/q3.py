massas = []
segundos = []
seg = 0

for i in range(0,3):
    print("Preencha com a massa em gramas de 10 materiais: {}" .format(i+1))
    m = int(input("Massa: "))
    if(m>0.10):
        massas.append(m)
    else:
        print("\nDigite massa superior a 0.10")

for i in range(0,3):
    j = massas[i]
    while j > 0.10:
        j = (25*j)/100
        seg = seg + 30
    segundos.append(seg)

print("Tempo em segundos para o decaimento das massas", segundos)

