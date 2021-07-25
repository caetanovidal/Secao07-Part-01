# https://www.youtube.com/watch?v=LiDkOQtcEGo me ajudou a fazer o cod

n = int(input('informe um numero: '))


def pascal(linha, coluna):
    if coluna == 0:                         # Todo começo de linha queremos retornar 1, e todo começo tem a coluna = 0
        return 1
    if linha == coluna:                     # Aqui é como se fosse a diagonal principal de um quadrado, a qual forma um
        return 1                            # triangulo retangulo queremos tbm que seja sempre 1
    upLeft = pascal(linha - 1, coluna - 1)  # ACESSANDO O ELEMENTO ACIMA NA ESQUERDA
    upRigth = pascal(linha - 1, coluna)     # ACESSANDO O ELEMENTO ACIMA
    return upLeft + upRigth                 # Somando o elemento acima esquerda com o acima, resultando no proximo
                                            # numero da piramede


for l in range(0, n + 1):
    for c in range(0, n + 1):
        if c > l:                           # eliminando tudo que esta acima da diagonal principal!
            break
        print(pascal(l, c), end=' ')        # executando a funcao
    print()
