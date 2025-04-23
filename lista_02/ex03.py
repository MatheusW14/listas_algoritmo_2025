"""Crie um programa que faça uma contagem regressiva, do número fornecido até 0, utilizando
laços de repetição."""

N = int(input("Digite um numero: "))

for i in range(N, -1, -1):
    print(i)
