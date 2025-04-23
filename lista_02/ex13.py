"""Crie um programa usando apenas laços que calcule o MDC (Máximo Divisor Comum)
entre dois números inteiros fornecidos pelo usuário."""

N1 = int(input("Digite um numero inteiro: "))
N2 = int(input("Digite outro numero inteiro: "))


divisores_n1 = []
divisores_n2 = []

for i in range(1, N1):
    if N1 % i == 0:
        divisores_n1.append(i)

for i in range(1, N2):
    if N2 % i == 0:
        divisores_n2.append(i)

MDC = []

for divisor in divisores_n1:
    if divisor in divisores_n2:
        MDC.append(divisor)

if MDC:
    print(f"{max(MDC)}")
else:
    print("Não há divisores em comum.")
