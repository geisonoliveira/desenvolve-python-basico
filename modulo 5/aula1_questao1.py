from builtins import round

try:
    a = float(input("Digite o primeiro número: ").replace(',', '.'))
    b = float(input("Digite o segundo número: ").replace(',', '.'))
except ValueError:
    print("Entrada inválida.")
else:
    print(f"Diferença absoluta: {round(abs(a - b), 2):.2f}")