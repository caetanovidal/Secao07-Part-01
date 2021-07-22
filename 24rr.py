numero = []
altura = []
maior = 0
menor = 99
posicao = 0
posicao_menor = 0

for i in range(1, 11):
    num = int(input(f'informe o ({i}/10) numero do aluno: '))
    numero.append(num)

    alt = float(input(f'informe a ({i}/10) altura do aluno: '))
    altura.append(alt)

for x in range(0, len(numero)):
    if altura[x] > maior:
        maior = altura[x]
        posicao = x
    if altura[x] < menor:
        menor = altura[x]
        posicao_menor = x

print(f'maior altura = {maior} metros')
print(f'posicao = {numero[posicao]}')
print()
print(f'menor altura = {menor} metros')
print(f'posicao = {numero[posicao_menor]}')


