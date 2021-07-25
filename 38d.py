veetor = []

while len(veetor) < 10:
    num = int(input(f'informe um {len(veetor) + 1}/10 numero: '))
    veetor.append(num)

print(sorted(veetor))
