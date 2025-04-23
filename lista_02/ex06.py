"""Faça um programa que calcule o fatorial de um número inteiro positivo usando apenas
laços."""

N = int(input("Digite um número: "))
fatorial = 1

for i in range(N, 0, -1):
    fatorial *= i

print(f"O fatorial de {N} é: {fatorial}")
