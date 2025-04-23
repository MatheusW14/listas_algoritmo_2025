"""Sendo conhecidos os valores de z e w, calcular y:"""

Z = float(input("Digite um valor para Z: "))
W = float(input("Digite um valor para W: "))

if W > 0 or Z < 7:
    X = (5 * W + 1) / 3
    T = 5 * Z + 2
else:
    X = 5 * Z + 2
    T = (5 * W + 1) / 3

Y = (7 * X * 2 - 3 * X - 8 * T) / (5 * (X + 1))
print(f"{Y:.2f}")
