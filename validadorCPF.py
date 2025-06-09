import re

while True:
    cpf = input("Digite seu CPF: ");
    cpfNumeros = re.sub(r'\D', '', cpf);

    if len(cpfNumeros) != 11:
        print("Insira um cpf válido.\n")
        continue

    p1 = sum(int(cpfNumeros[i]) * (10 - i) for i in range(9))
    #sum (soma) i in range(0, 8)

    p2 = p1 * 10
    validacacao1 = p2 % 11
    if validacacao1 == 10:
        validacacao1 = 0

    if int(cpfNumeros[9]) == validacacao1:
        print('Primeira verificação concluída!')
    else:
        print("Primeira verificação falhou!\n")
        print("Insira um cpf válido.")
        continue

    t1 = sum(int(cpfNumeros[i]) * (11 - i) for i in range(10)) #316

    t2 = t1 * 10
    validacacao2 = t2 % 11 #3
    if validacacao2 == 10:
        validacacao2 = 0

    if int(cpfNumeros[10]) == validacacao2:
        print("Segunda verificação concluída!\n\n")
        break
    else:
        print("Segunda verificação falhou!\n")
        print("Insira um cpf válido.")
        continue

print("CPF VÁLIDO!")