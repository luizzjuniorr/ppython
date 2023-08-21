sa = float(input("Digite seu salário: "))

if sa>=0 and sa<=1000:
    print(f"Novo salario = R$ {sa*0.2+sa}")
    print(f"Aumento = R$ {sa*0.2}")
    print("O aumento foi de 20%")

elif sa>=1001 and sa<=3000:
    print(f"Novo salario = R$ {sa*0.15+sa}")
    print(f"Aumento = R$ {sa*0.15}")
    print("O aumento foi de 15%")

elif sa>=3001 and sa<=8000:
    print(f"Novo salario = R$ {sa*0.1+sa}")
    print(f"Aumento = R$ {sa*0.1}")
    print("O aumento foi de 10%")

elif sa>=8001:
    print(f"Novo salario = R$ {sa*0.05+sa}")
    print(f"Aumento = R$ {sa*0.05}")
    print("O aumento foi de 5%")