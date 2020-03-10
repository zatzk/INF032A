x=1
cont=0
while x != 0:
    num = int(input())
    if num > 100 and num < 200:
        cont = cont +1

    print(cont)
    if num == 0:
        x=0
