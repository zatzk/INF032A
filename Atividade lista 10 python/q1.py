produtos = []
i=0
mercmenos = 0
mercmeio = 0
mercmais = 0

for i in range(0,100):
    print("Insira nome e precos do produto {}" .format(i+1))
    nome = input("Nome: ")
    pc = int(input("preço compra: "))
    pv = int(input("preço venda: "))

    perC10 = (10*pc)/100
    perC20 = (20*pc)/100
    
    lucro = (pv-pc)

    if (lucro<perC10):
        mercmenos+=1
        
        
    elif (lucro>perC20):
        mercmais+=1
        

    elif (lucro>=perC10) and (lucro<=perC20):
        mercmeio+=1
        

    

print("Total de produtos que lucraram abaixo de 10% {}" .format(mercmenos))
print("Total de produtos que entre 10% e 20% {}" .format(mercmeio))
print("Total de produtos que lucraram acima de 20% {}" .format(mercmais))
