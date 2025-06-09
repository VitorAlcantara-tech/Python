num = int(input('Digite um número: '));

if num % 2 == 0:
    print(f"O número {num} é par.\n\n");

else: 
    print(f"O número {num} é ímpar.\n\n");


a = int(input("Digite o primeiro número: "));
b = int(input("Digite o segundo número: "));

soma = a + b;
print(f"A soma dos números {a} e {b} é igual a {soma}\n\n");

c = int(input("Digite o primeiro número: "));
d = int(input("Digite o segundo número: "));

if c > d:
    print(f"{c} é maior que {d}.\n\n");
elif d > c:
    print(f"{d} é maior que {c}.\n\n");
else:
    print("Os número são iguais.\n\n");

idade = int(input("Digite a sua idade: "));
if idade < 18:
    print("Menor de idade. \n\n");
elif idade < 59:
    print("Adulto");
else:
    print("Idoso");