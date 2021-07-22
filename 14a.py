vetor = []
vetor_reps = []

for i in range(1, 11):
    n = int(input(f'informe um ({i}/10) numero: '))
    if n not in vetor:
        vetor.append(n)
    elif n not in vetor_reps:
        vetor_reps.append(n)
        vetor.append(n)
print(f'Numeros repetidos = ', end='')
for x in vetor_reps:
    print(f'{x}', end=', ')
