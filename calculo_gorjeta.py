
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

valor = 150.0
porcentagem = 10

resultado = calcular_gorjeta(valor, porcentagem)
print(f"Gorjeta: R$ {resultado:.2f}")