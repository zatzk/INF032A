bruto = int(input())
prestacao = int(input())

percent = (bruto * 35) / 100

if prestacao > percent:
    print('a prestacao nao pode ser concedida')
if prestacao < percent:
    print('a prestacao sera disponibilizada')
