# ORDENACAO MANUAL
# Solicita 5 números ao usuário
numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Ordenação manual - Método da Bolha (Bubble Sort)
n = len(numeros)

for i in range(n):
    for j in range(0, n - i - 1):
        if numeros[j] > numeros[j + 1]:
            # Troca os elementos
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

# Exibe os números ordenados
print("Números ordenados:", numeros)
