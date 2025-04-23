"""Crie um programa usando laços que receba uma frase do usuário e retorne quantas vogais
há nessa frase."""

frase = input("Digite uma frase: ")

VOGAIS = "AEIOUaeiou"

vogais_texto = []

for letra in frase:
    if letra == VOGAIS:
        vogais_texto.append(letra)
print(f"A quantidade de vogais e: {len(vogais_texto)}")
