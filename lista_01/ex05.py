"""
Calcular o valor do salario liquido de um programador
, dado o numero funcoes criadas, valor de cada funcao, o percentual de desconto do INSS e 8% sobre o salario bruto.
Devera ser informado o nome do funcionario, o salario bruto o salario liquido. Validar os valores de entrada
"""

nome_programador = input("Digite o nome do programador: ")

funcoes_criadas = int(
    input("Digite a quantidade de funções realizadas por este programador: ")
)

valor_funcoes = float(input("Digite o valor de cada função: "))

salario_bruto = funcoes_criadas * valor_funcoes

salario_liquido = salario_bruto - salario_bruto * 0.08

print(
    f"O programador {nome_programador} recebe um salario bruto de R$ {salario_bruto} e um salario liquido de R$ {salario_liquido}."
)
