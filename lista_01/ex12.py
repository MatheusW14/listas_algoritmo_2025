"""Determinar, dentre quarto numeros, a soma dos pares"""

numeros = []
for i in range(4):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
num_pares = []
for numero in numeros:
    if int(numero) % 2 == 0:
        num_pares.append(numero)
soma_pares = sum(num_pares)
print(f"A soma dos números pares é: {soma_pares}")
