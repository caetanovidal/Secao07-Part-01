vetor = []
vetor_par = []
vetor_impar = []

while len(vetor) < 6:
    num = int(input("informe um numero: "))
    vetor.append(num)

for x in vetor:
    if x % 2 == 0:
        vetor_par.append(x)
    else:
        vetor_impar.append(x)

print(f'Numeros pares = {vetor_par}')
print(f'Soma dos numeros pares = {sum(vetor_par)}')
print(f'Numeros impares = {vetor_impar}')
print(f'Quantidade de numeros impares = {len(vetor_impar)}')
