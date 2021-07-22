lista = []

while len(lista) < 8:
    n = int(input("informe um numero: "))
    lista.append(n)
j = int(input("informe uma posicao: "))
k = int(input("informe uma posicao: "))

soma = lista[j] + lista[k]
print(soma)
