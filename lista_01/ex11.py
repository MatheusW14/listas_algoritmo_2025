import math

a = float(input("Digite o coeficiente A (diferente de 0): "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

if a == 0:
    print("O coeficiente A deve ser diferente de 0.")
else:
    delta = b**2 - 4 * a * c

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"A equação possui uma única raiz real: {raiz}")
    else:
        raiz_quadrada_delta = math.sqrt(delta)
        raiz1 = (-b + raiz_quadrada_delta) / (2 * a)
        raiz2 = (-b - raiz_quadrada_delta) / (2 * a)
        print(f"As raízes reais da equação são: {raiz1} e {raiz2}")
