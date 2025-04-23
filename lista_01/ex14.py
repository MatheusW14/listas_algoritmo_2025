"""colocar 3 valores em ordem crescente"""

lista_numeros = []

for i in range(3):
    num = float(input(f"Digite o {i+1}º numero:"))
    lista_numeros.append(num)

lista_crescente = sorted(lista_numeros)
print(f"Os valores em ordem crescente são: {lista_crescente:.2f}")
