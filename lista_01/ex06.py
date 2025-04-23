"""
ler dois valores maiores que zero para as variáveis A e B.
efetuar a troca de conteudos de forma que a variável A passe a ter o conteúdo da variável B
e vice-versa. Utilize 1 variével AUX para resolver"""

var_a = float(input("Digite um valor maior que 0 para a variavel A: "))
var_b = float(input("Digite um valor maior que 0 para a variavel B: "))

aux = var_a
var_a = var_b
var_b = aux

if var_a < 0 and var_b < 0:
    print("Erro, valor menor que zero.")
else:
    print(f"As variáveis são A:{var_a} e B:{var_b}")
