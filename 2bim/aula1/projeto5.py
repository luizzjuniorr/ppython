n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota: "))
n3 = float(input("Digite a 3° nota: "))
n4 = float(input("Digite a 4° nota: "))
n5 = float(input("Digite a 5° nota: "))

nf = (n1+n2+n3+n4+n5)/5

if nf>=6:
    print(f"APROVADO com média = {nf:.2f}")

else:
    print(f"REPROVADO com média = {nf:.2f}")