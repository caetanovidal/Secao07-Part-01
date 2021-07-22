vetor = []

for i in range(1, 21):
    num = int(input(f'informe ({i}/20) o numero do aluno: '))
    if num not in vetor:
        vetor.append(num)
print(vetor)
