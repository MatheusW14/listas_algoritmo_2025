"""Dado um valor inteiro positivo n, imprima os primeiros n termos da sequência de Fibonacci
em ordem decrescente utilizando apenas laços de repetição."""

n = int(
    input(
        "Digite um número inteiro positivo para os primeiros n termos da sequência de Fibonacci: "
    )
)

fibonacci = []

a, b = 0, 1
for _ in range(n):
    fibonacci.append(a)
    a, b = b, a + b

print("Sequência de Fibonacci em ordem decrescente:")
for i in range(len(fibonacci) - 1, -1, -1):
    print(fibonacci[i], end=" ")
