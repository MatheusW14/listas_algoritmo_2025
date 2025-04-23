"""Calcular a area de uma circunferencia e mostra-la. Formula: Area= pi*r^."""

raio = float(
    input("Digite um numero para o raio, e te retornaremos a área da circunferência: ")
)

PI = 3.1416
AREA = PI * (raio * raio)

if raio <= 0:
    print("Erro, o numero precisa ser maior que 0.")
else:
    print(f"{AREA:.2f}")
