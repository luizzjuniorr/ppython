#ex 14

cf = input("Voce vai digitar a temperatura em qual escala (C/F)? ")

if cf == "f":
    fr = float(input("Digite a temperatura em Fahrenheit: ") )
    print(f"Temperatura equivalente em Celsius: {(5/9)*(fr-32):.2f}")

if cf == "c":
    cl = float(input("Digite a temperatura em Celsius: "))
    print(f"Temperatura equivalente em Fahrenheit: {cl*(9/5)+32:.2f}") 