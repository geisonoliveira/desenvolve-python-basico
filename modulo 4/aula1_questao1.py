x = int(input("Digite um número: "))

if x > 5:
    while x > 5:
        print("Maior que 5")
        x -= 1
elif x <= 0:
    while x <= 5:
        print("Menor que 5")
        x += 1

print("Fim")