def print_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 10)

def verificar_vitoria(tabuleiro, jogador):
    # Checar linhas
    for linha in tabuleiro:
        if all(espaco == jogador for espaco in linha):
            return True
    # Checar colunas
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    # Checar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def verificar_empate(tabuleiro):
    return all(all(espaco != ' ' for espaco in linha) for linha in tabuleiro)

def jogar():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'

    while True:
        print_tabuleiro(tabuleiro)
        try:
            linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1 ou 2): "))
            coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1 ou 2): "))
        except ValueError:
            print("Entrada inválida. Use números 0, 1 ou 2.")
            continue
        
        if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
            print("Linha ou coluna inválida. Escolha entre 0, 1 ou 2.")
            continue
        
        if tabuleiro[linha][coluna] != ' ':
            print("Posição já ocupada! Escolha outra.")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            print_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            print_tabuleiro(tabuleiro)
            print("Empate!")
            break

        # Alterna entre os jogadores
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

if __name__ == "__main__":
    jogar()

# NAO ENTENDI NADA DESSE