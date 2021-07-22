lista = []
maior = -9999
menor = 9999
while len(lista) < 10:
    n = int(input(f'informe um ({len(lista) + 1}/10) numero: '))
    lista.append(n)
for x in lista:
    if x < menor:
        menor = x
    if x > maior:
        maior = x
print(maior)
print(menor)

print(f'o maior esta na posiçao {lista.index(maior)}')
print(f'o menor esta na posicao {lista.index(menor)}')
