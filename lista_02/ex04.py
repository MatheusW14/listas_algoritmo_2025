"""Crie um programa que imprima todos os números pares até o número fornecido pelo
usuário usando laços."""

N = int(input("Digite um numero: "))

for i in range(N + 1):
    if i % 2 == 0:
        print(f"{i}")
