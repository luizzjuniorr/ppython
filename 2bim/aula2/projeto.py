ns1= float(input("Digite a primeira nota:: "))
ns2= float(input("Digite a segunda nota:: "))

nf = ns1+ns2

if nf>=60:
    print(f"NOTA FINAL = {nf:.1f}")
else:
    print(f"NOTA FINAL = {nf:.1f}")
    print("REPROVADO")