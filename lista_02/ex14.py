"""Utilizando apenas laços de repetição, imprima uma pirâmide de números palíndromos com
altura n."""

N = 4

for i in range(1, N + 1):
    for j in range(1, N - i + 1):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
