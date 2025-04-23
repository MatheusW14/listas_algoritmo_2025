"""Faça um programa que some apenas os números ímpares até um número inteiro positivo
informado pelo usuário usando laços."""

N = int(input("Digite um numero: "))
soma = 0

for i in range(N + 1):
    if i % 2 != 0:
        soma += i
print(soma)
