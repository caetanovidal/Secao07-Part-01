vetor = []
soma = []
qtd_neg = []

for i in range(1, 11):
    n = int(input(f'informe o ({i}/10) numero: '))
    vetor.append(n)
    if n > 0:
        soma.append(n)
    else:
        qtd_neg.append(n)
print(sum(soma))
print(len(qtd_neg))
