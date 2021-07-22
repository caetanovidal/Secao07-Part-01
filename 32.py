vetorx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetory = [3, 2, 1, 4, 6, 7, 9, 5, 2, 1]


print('soma = ', end='')
for x in range(0, len(vetorx)):
    soma = vetorx[x] + vetory [x]
    print(f'{soma}', end=', ')

print()
print('produto = ', end='')
for x in range(0, len(vetorx)):
    produto = vetorx[x] * vetory [x]
    print(f'{produto}', end=', ')

s = set(vetorx)
s1 = set(vetory)

diferenca = s.difference(s1)
print()
print(diferenca)

intersecao = s.intersection(s1)
print(intersecao)

uniao = s.union(s1)
print(uniao)
