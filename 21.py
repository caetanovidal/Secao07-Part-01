vetorA = []
vetorB = []
vetorC = []

for i in range(1, 11):
    a = int(input(f'informe um ({i}/10) um numero para o vetor A: '))
    b = int(input(f'informe um ({i}/10) um numero para o vetor B: '))
    vetorA.append(a)
    vetorB.append(b)
    c = a - b
    vetorC.append(c)
print(vetorC)
