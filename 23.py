vetorA = []
vetorB = []
vetorC = []

for i in range(1, 11):
    a = int(input(f'informe um ({i}/10) um numero para o vetor A: '))
    b = int(input(f'informe um ({i}/10) um numero para o vetor B: '))
    vetorA.append(a)
    vetorB.append(b)
    c = a * b
    vetorC.append(c)
print(f'Vetor 1 = {vetorA}')
print(f'Vetor 2 = {vetorB}')
print(f'produto entre os elementos de cada vetor:\n'
      f'          {vetorC}')
