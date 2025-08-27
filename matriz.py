def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append('.')
        matriz.append(linha)
    return matriz

def diagonal(tamanho):
    matriz = criar_matriz(tamanho, tamanho)
    for i in range(tamanho):
        matriz[i][-i -1] = 'x'
        matriz[i][i] = 'x'
            
    return matriz

def matriz_bordas(linha, coluna):
    matriz = criar_matriz(linha, coluna)
    for i in range(coluna):
        matriz[0][i]= 'x'
    for i in range(coluna):
        matriz[linha-1][i] = 'x'
    return matriz
        


from pprint import pprint

# pprint(diagonal(7))
pprint(matriz_bordas(5, 5))