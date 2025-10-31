distancia = float(input("Insira a distância em KM: "))
if distancia < 0 or distancia == 0:
    print("Distância inválida.")
peso = float(input("Insira o peso em KG: "))
if peso < 0 or peso == 0:
    print("Peso inválido.")
if distancia <= 100:
    custo = peso * 1.00
    if peso > 10:
        custo += 10.00
    print(f"O custo do frete é: R$ {custo:.2f}")
elif distancia > 100 or distancia <= 300:
    custo = peso * 1.50
    if peso > 10:
        custo += 10.00
    print(f"O custo do frete é: R$ {custo:.2f}")
elif distancia > 300:
    custo = peso * 2.00
    if peso > 10:
        custo += 10.00
    print(f"O custo do frete é: R$ {custo:.2f}")