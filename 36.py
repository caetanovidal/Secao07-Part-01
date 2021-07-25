vetor = []

while len(vetor) < 10:
    num = int(input(f'Informe um ({len(vetor) + 1}/10)numero: '))
    vetor.append(num)

print(sorted(vetor))


