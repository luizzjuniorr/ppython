#ex18
c = input("Informe o combustível (G/A): ")
lt = float(input("Informe a quantidade: "))

if c == "G":
    if lt >= 1 and lt <= 20:
        pr = 2.5 * lt
        print(f"Valor a pagar: {pr - (pr * 0.25)}")
    if lt >=21:
        pr = 2.5 * lt
        print(f"Valor a pagar: {pr - (pr * 0.65)}")
    
if c == "A":
    if lt >= 1 and lt <= 20:
        pr = 1.9 * lt
        print(f"Valor a pagar: {pr - (pr * 0.35)}")     
    if lt >= 21:
        pr = 1.9 * lt
        print(f"Valor a pagar: {pr - (pr * 0.5)}")     