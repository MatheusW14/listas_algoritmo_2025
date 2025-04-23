"""Verifique se um triângulo é retângulo, acutângulo ou obtusângulo"""

a = float(input("Digite o valor do primeiro lado: "))
b = float(input("Digite o valor do segundo lado: "))
c = float(input("Digite o valor do terceiro lado: "))

if a < b + c and b < a + c and c < a + b:
    lados = sorted([a, b, c])
    a, b, c = lados[0], lados[1], lados[2]

    if c**2 == a**2 + b**2:
        print(
            "Triângulo Retângulo"
        )  # O quadrado do maior lado é igual à soma dos quadrados dos outros dois lados.
    elif c**2 < a**2 + b**2:
        print(
            "Triângulo Acutângulo"
        )  # O quadrado do maior lado é menor que a soma dos quadrados dos outros dois lados.
    else:
        print("Triângulo Obtusângulo")
else:
    print("Triângulo inválido.")
