import random

print("Jogo de adivinhalçao do número secreto.\n");
numAleatorio = random.randint(1, 100); #Gera número aleatório random.randint
chute = int(input("Digite o número secreto: "));

tentativas = 1;


while chute != numAleatorio: #Enquanto chute for diferente de numAleatorio
    if chute < numAleatorio:
        print(f"O número secreto é maior que {chute}.");
        chute = int(input("Digite o número secreto: "));
        tentativas += 1;

    elif chute > numAleatorio:
        print(f"O número secreto é menor que {chute}.");
        chute = int(input("Digite o número secreto: "));
        tentativas += 1;
        
if chute == numAleatorio:
    if tentativas > 1:
        print(f"Parabéns você acertou o número secreto em {tentativas} tentativas.");
    else:
        print(f"Parabéns você acertou o número secreto em {tentativas} tentativa.");
