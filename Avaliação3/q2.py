resultado = []


for i in range(0,3):
    print("Insira os valores a serem calculados: {} " .format(i+1))
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    
    if(dividendo>divisor):
       
       resto = dividendo % divisor
       resultado.append(resto)
        
    else:
        print("\ndividendo tem que ser maior que divisor")
    

print("resto das divisões", resultado)
