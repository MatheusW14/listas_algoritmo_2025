"""Dado um numero, informe em qual dos intervalos ele se encontra."""

num = int(input("Digite um numero inteiro para saber em qual intervalo ele se encontra: "))

if num in range(0, 20):
    print("O numero esta no intervalo A(0, 20).")
elif num in range(-5, -1) and num in range(-100, 15):
    print("O numero esta no intervalo B(-5, -1) e no intervalo D(-100, 15)")
elif num in range(20, 60):
    print("O numero esta no intervalo C(20, 60).")
elif num in range(-100, 15):
    print("O numero esta no intervalo D(-100, 15).")
else:
    print("O numero nao esta em nenhum dos intervalos.")
