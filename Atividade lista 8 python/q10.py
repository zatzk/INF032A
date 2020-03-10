for i in range(0,10):
    num = float(input("Digite um número:\n"))
    if num < 0:
        print('numero menor que 0')
    if num > 0:
        raiz = float(num) ** 0.5
        print(f'\nA raiz quadrada de {num} é {raiz}\n')
