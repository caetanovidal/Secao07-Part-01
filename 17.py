vetor = []

for x in range(1, 11):
    n = int(input(f'informe um ({x}/10) numero: '))
    if n < 0:
        n = 0
    vetor.append(n)
for i in vetor:
    print(i, end=' ')
