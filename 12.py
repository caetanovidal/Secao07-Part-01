vetor = []

for i in range(1, 6):
    n = int(input(f'informe o ({i}/5) numero: '))
    vetor.append(n)
for x in vetor:
    print(x, end=' ')
print(max(vetor))
print(min(vetor))
print(sum(vetor) / len(vetor))
