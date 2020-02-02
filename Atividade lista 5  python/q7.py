a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

if b > a and b < c:
    intermediario = b
if b < a and b > c:
    intermediario = b

if a > b and a < c:
    intermediario = a
if a < b and a > c:
    intermediario = a

if c > a and c < b:
    intermediario = c
if c < a and c > b:
    intermediario = c

if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(menor, intermediario, maior)
