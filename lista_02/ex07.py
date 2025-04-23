"""Faça um programa que conte quantos divisores inteiros um número inteiro positivo possui
utilizando laços."""

N = int(input("Digite um numero para descobrir seus divisores: "))

divisores = []

for i in range(1, N + 1):
    if N % i == 0:
        divisores.append(i)
print(N)
