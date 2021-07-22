vetor = []

cod = int(input("informe um codigo: "))

while cod != 1 and cod != 2:
    print("informe um codigo valido")
    cod = int(input("informe um codigo: "))

for i in range(1, 6):
    n = int(input(f'informe um ({i}/5) numero: '))
    vetor.append(n)
if cod == 1:
    for x in vetor:
        print(x, end=' ')
if cod == 2:
    for x in range(4, -1, -1):
        print(vetor[x], end=' ')

