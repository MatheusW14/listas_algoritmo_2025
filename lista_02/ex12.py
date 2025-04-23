"""Faça um programa que, utilizando laços, imprima o seguinte padrão numérico invertido
baseado no número inteiro informado pelo usuário."""

N = int(input("Digite um numero: "))

for i in range(N, -1, -1):
    print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end="")
    print(" ")
