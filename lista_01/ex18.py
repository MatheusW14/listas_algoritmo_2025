saldo_medio = float(input("Digite o saldo médio do último ano: "))

if saldo_medio <= 200:
    credito = 0
    mensagem = "Nenhum crédito"
elif 201 <= saldo_medio <= 400:
    credito = saldo_medio * 0.20
    mensagem = "20% do valor do saldo médio"
elif 401 <= saldo_medio <= 600:
    credito = saldo_medio * 0.30
    mensagem = "30% do valor do saldo médio"
else:
    credito = saldo_medio * 0.40
    mensagem = "40% do valor do saldo médio"

print(f"\nSaldo médio: R$ {saldo_medio:.2f}")
print(f"Valor do crédito: R$ {credito:.2f}")
print(f"Critério: {mensagem}")
