from collections import deque
lista1 = []

lista = deque()
inverso = deque()
while len(lista) < 6:
    n = int(input(f'informe um ({len(lista) + 1}/6) numero: '))
    lista.append(n)
    lista1.append(n)

# forma 1
print(lista1[::-1])

# forma 2
for x in lista:
    inverso.appendleft(x)
print(inverso)
