"""Faça um programa que imprima a seguinte série incremental, com base num valor n:"""

N = int(input("Digite um numero: "))

for i in range(1, N + 1):
    print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end="")
    print(" ")
