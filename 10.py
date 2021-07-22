notas = []
soma = 0
for i in range(1, 16):
    n = int(input(f'informe a nota do aluno numero {i}: '))
    notas.append(n)
print(notas)
# print(sum(notas)/len(notas))  -> jeito facil

for x in notas:
    soma += x
print(soma/15)
