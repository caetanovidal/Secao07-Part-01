vetor = []
maior = -999
menor = 999
posicao = 0
posicao_min = 0
for i in range(1, 6):
    n = int(input(f'informe o ({i}/5) numero: '))
    vetor.append(n)
    if n > maior:
        maior = n
        posicao = i
    if n < menor:
        menor = n
        posicao_min = i
print(f'o maior é {maior} e esta na posicao {posicao}')
print(f'o menor é {menor} e esta na posicao {posicao_min}')
print(vetor.index(maior + 1))# posicao do maior...
print(vetor.index(menor + 1))# Posicao menor...
