lista = []
pares = []
while len(lista) < 10:
    n = int(input(f'informe um ({len(lista)+ 1}/10) numero: '))
    lista.append(n)
for x in lista:
    if x % 2 == 0:
        pares.append(x)
print(len(pares))
print(pares)
