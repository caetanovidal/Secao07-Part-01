from collections import Counter

vetor = []

for i in range(1, 11):
    n = int(input(f'informe um ({i}/10) numero: '))
    vetor.append(n)

repetidos = Counter(vetor)

for x in repetidos:
    if repetidos[x] > 1:
        print(f'O numero {x} foi repetido {repetidos[x]} vezes')
print(vetor)



