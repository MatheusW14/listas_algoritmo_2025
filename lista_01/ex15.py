"""Dadas 3 medidas, verificar se elas podem ser os comprimentos dos lados de um triangulo,
se forem, verificar se e equilatero, isoceles(dois lados iguais) ou escaleno(todos os lados diferentes).
O triangulo e uma figura geometrica fechada de tres lados, em que cada um e menor que a soma dos outros dois.
"""

a = float(input("Digite o valor do primeiro lado: "))
b = float(input("Digite o valor do segundo lado: "))
c = float(input("Digite o valor do terceiro lado: "))


if a < b + c and b < a + c and c < a + b:
    if a == b and a == c:
        print("Este é um triângulo equilátero.")
    elif a == b and a != c or a == c and a != c:
        print("Este é um triângulo isóceles.")
    else:
        print("Este é um triângulo escaleno.")
else:
    print("Triangulo invalido.")
