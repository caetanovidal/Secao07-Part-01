vetorA = []
vetorB = []
vetorC = []

for i in range(1, 11):
    a = int(input(f'informe um ({i}/10) um numero para o vetor A: '))
    b = int(input(f'informe um ({i}/10) um numero para o vetor B: '))
    vetorA.append(a)
    vetorB.append(b)
    if i % 2 == 0:
        vetorC.append(a)
    else:
        vetorC.append(b)

print(vetorC)
