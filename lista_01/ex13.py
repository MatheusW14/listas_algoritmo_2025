"""Obter , dentre cinco numeros, a media dos impares"""

numeros = []
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

num_impar = []
for numero in numeros:
    if int(numero) % 2 == 1:
        num_impar.append(numero)

if num_impar:
    media_impares = sum(num_impar) / len(num_impar)
    print(f"A média dos numeros ímpares é: {media_impares}.")
else:
    print("Não há números ímpares na lista.")
