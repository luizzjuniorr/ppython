n1 = 5.00
n2 = 3.50
n3 = 4.80
n4 = 8.90
n5 = 7.32

cd = int(input("Codigo do produto comprado: "))
qnt = int(input("Quantidade comprada: "))
if cd == 1:
    print(f"Valor a pagar: {n1*qnt}")
elif cd == 2:
    print(f"Valor a pagar: {n2*qnt}")
elif cd == 3:
    print(f"Valor a pagar: {n3*qnt}")
elif cd == 4:
    print(f"Valor a pagar: {n4*qnt}")
elif cd == 5:
    print(f"Valor a pagar: {n5*qnt}")