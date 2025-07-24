import re
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_inicial():
    while True:
        limpar_tela()
        print("=" * 45)
        print("   VALIDADOR DE CPF  -  Vitor Alcantara ")
        print("=" * 45)
        print("1 - Iniciar Validação")
        print("2 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            validar_cpf()
        elif opcao == '2':
            print("Saindo...")
            break
        else:
            input("Opção inválida. Pressione ENTER para tentar novamente.")

def validar_cpf():
    while True:
        cpf = input("\033[0mDigite seu CPF:");
        cpfNumeros = re.sub(r'\D', '', cpf);
    # re.sub(...) → substitui caracteres com base em um padrão
    # r'\D' → é a expressão regular que **representa tudo que não é dígito 
    # '' → substitui esses caracteres por nada (remove)
    # cpf → é a string que o usuário digitou

        if len(cpfNumeros) != 11:
            print("\033[31mInsira um cpf válido.\n")
            continue

        p1 = sum(int(cpfNumeros[i]) * (10 - i) for i in range(9))
    #sum (soma) i in range(0, 9)

        p2 = p1 * 10
        validacacao1 = p2 % 11
        if validacacao1 == 10:
            validacacao1 = 0

        if int(cpfNumeros[9]) == validacacao1:
            print('✅ Primeira verificação concluída!')
        else:
            print("❌ Primeira verificação falhou!\n")
            print("\033[31mCPF INVÁLIDO.\n")
            continue

        t1 = sum(int(cpfNumeros[i]) * (11 - i) for i in range(10)) #316

        t2 = t1 * 10
        validacacao2 = t2 % 11 #3
        if validacacao2 == 10:
            validacacao2 = 0

        if int(cpfNumeros[10]) != validacacao2:
            print("❌ Segunda verificação falhou!\n")
            print("\033[31mCPF INVÁLIDO.\n")
            continue
        else:
            print("✅ Segunda verificação concluída!\n")

        print("\033[32mCPF VÁLIDO!\n")
        input("\033[0mPressione ENTER para voltar ao menu.")
        break

menu_inicial()