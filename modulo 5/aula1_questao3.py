import random

numero = random.randint(1, 10)

while True:
    entrada = input("Adivinhe o número (1-10): ").strip()
    try:
        palpite = int(entrada)
    except ValueError:
        print("Entrada inválida. Digite um inteiro entre 1 e 10.")
        continue

    if palpite < 1 or palpite > 10:
        print("Escolha um número entre 1 e 10.")
        continue

    if palpite < numero:
        print("Muito baixo.")
    elif palpite > numero:
        print("Muito alto.")
    else:
        print("Correto! Você acertou.")
        break