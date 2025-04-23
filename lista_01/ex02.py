"""Dado um numero, verifique se ele esta no intervalo de 100 a 1000."""

num = int(input("Digite um numero para verficar se ele esta entre 100 e 1000: "))

if num in range(100, 1000):
    print("O numero esta no intervalo entre 100 e 1000.")
else:
    print("O numero nao esta no intervalo entre 100 e 1000")
