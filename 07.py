lista = []

while len(lista) < 10:
    n = int(input(f'informe um ({len(lista) + 1}/10) numero: '))
    lista.append(n)
print(max(lista))
print(f'o maior esta na posiçao {lista.index(max(lista))}')

