"""Dadas 3 medidas, informar a maior."""

medida_1 = float(input("Digite a primeira medida: "))
medida_2 = float(input("Digite a segunda medida: "))
medida_3 = float(input("Digite a terceira medida: "))

if medida_1 > medida_2 and medida_1 > medida_3:
    print("A maior medida é a 1.")
elif medida_2 > medida_1 and medida_2 > medida_3:
    print("A maior medida é a 2.")
elif medida_3 > medida_1 and medida_3 > medida_2:
    print("A maior medida é a 3.")
else:
    print("Existem medidas iguais.")
