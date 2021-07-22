vetor = []

for i in range(1, 11):
    n = int(input(f'informe um ({i}/10) numero: '))
    vetor.append(n)

vetor_x = []

x = int(input("informe um numero x: "))

for z in vetor:
    if z % x == 0:
        vetor_x.append(z)

print(f'Multiplos do x = {vetor_x}')
if len(vetor_x) == 0:
    print("nao há multilos de x")
