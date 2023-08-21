n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))

if n1 % n2 == 0 or n2 % n1 == 0:
    print(f"são múltiplos")

else:
    print("não são múltiplos")