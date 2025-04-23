"""Faça um programa usando laços que some todos os números inteiros de 1 até n fornecido
pelo usuário"""

n = 5
soma = 0

for i in range(1, n + 1):
    soma += i

print(f"A soma dos números de 1 a {n} é: {soma}")
