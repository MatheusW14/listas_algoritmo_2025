"""Tendo como dados de entrada a altura e o sexo de uma pessoa, calcular seu peso ideal, utilizandoas seguintes formulas:
- para homens: (72,7 x H) - 58
- para mulheres: (62,1 x H) - 44,7"""

altura_pessoa = float(input("Digite a sua altura(Ex: 1.80): "))

calc_homem = (72.7 * altura_pessoa) - 58
calc_mulher = (62.1 * altura_pessoa) - 44.7

sexo = input("Digite o sexo(M ou F): ").upper()

if sexo == "M":
    print(f"O seu peso ideal é: {calc_homem:.2f}Kg. ")
elif sexo == "F":
    print(f"O seu peso ideal é: {calc_mulher:.2f}Kg. ")
else:
    print("Digite uma opção válida.")
