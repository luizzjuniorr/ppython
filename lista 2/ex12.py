# ex12

pp = float(input("Digite o valor do seu produto: "))
qnt = float(input("Digite a quantidade comprada: "))
dr = float(input("Digite o valor recebido: "))
valort = (pp*qnt)

if dr > valort:
    print(f"TROCO: {dr-valort}")

else:
    print(f"DINHEIRO INSUFICIENTE FALTA: {dr-valort}")