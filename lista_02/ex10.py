"""Faça um programa usando apenas laços que determine se um número informado pelo
usuário é um número perfeito. Um número é perfeito quando é igual à soma dos seus
divisores próprios (exceto ele mesmo).
"""

N = int(input("Digite um número para descobrir se ele é perfeito: "))

divisores = []

for i in range(1, N):
    if N % i == 0:
        divisores.append(i)

soma_divisores = sum(divisores)

if soma_divisores == N:
    print("Número Perfeito.")
else:
    print("Não é perfeito.")
