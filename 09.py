lista = []
while len(lista) < 6:
    n = int(input(f'informe um ({len(lista) + 1}/6)numero par: '))
    if n % 2 == 0:
        lista.append(n)
print(lista)
print(lista[::-1])


