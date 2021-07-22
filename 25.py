vetor = []
n = 0
while True:
    n += 1
    if n % 7 != 0 and n % 10 == 7:
        vetor.append(n)
    if len(vetor) == 100:
        break
print(vetor)
