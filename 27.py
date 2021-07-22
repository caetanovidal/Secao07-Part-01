n = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
contador = 0

index = 0
i = 2
primos = []
posicao = []
local = 0

while True:
    for i in range(1, 14):
        if n[index] % i == 0:
            contador += 1
    if contador == 2:
        primos.append(n[index])
        posicao.append(local)
        local += 1
        index += 1
    if contador >= 3:
        contador = 0
        index += 1
    if index == len(n):
        break

for x in range(0, len(primos)):
    print(f'primo = {primos[x]}', end=', ')
    print(f'na posicao {posicao[x]}')



