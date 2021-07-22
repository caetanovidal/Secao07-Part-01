vetor = []

while len(vetor) < 10:
    n = int(input(f'informe um ({len(vetor)+1}/10) numero: '))
    if n in vetor:
        vetor.remove(n)
    vetor.append(n)

print(vetor)
