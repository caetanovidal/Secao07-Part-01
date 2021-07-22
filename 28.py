v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v_impar = []
v_par = []

for num in v:
    if num % 2 == 0:
        v_par.append(num)
    else:
        v_impar.append(num)
print(f'Elementos impares = {v_impar}')
print(f'Elementos pares = {v_par}')
