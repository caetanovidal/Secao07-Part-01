vetor = []
vetor_impar = []
n = 0

posicao = 0
posicao_impar = 0
for i in range(1, 11):
    n = int(input(f'informe um ({i}/10) numero: '))
    while n < 0 or n > 50:
        n = int(input(f'informe um ({i}/10) numero entre 0 e 50: '))
    vetor.append(n)
    if n % 2 != 0:
        vetor_impar.append(n)

print("vetor: ")
while True:
    print(f'{vetor[posicao]}, {vetor[posicao + 1]}')
    posicao += 2
    if posicao >= 10:
        break
print()
print('vetor impar:')

while True:
    print(f'{vetor_impar[posicao_impar]}', end=', ')
    posicao_impar += 1

    if posicao_impar >= len(vetor_impar):
        break

    print(f'{vetor_impar[posicao_impar]}')
    posicao_impar += 1

    if posicao_impar >= len(vetor_impar):
        break





