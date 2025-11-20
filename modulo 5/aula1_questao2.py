import random
import math

try:
    n = int(input("Digite quantos números aleatórios quer gerar: "))
    if n <= 0:
        print("Deve ser um inteiro positivo.")
    else:
        valores = [random.randint(0, 100) for _ in range(n)]
        soma = sum(valores)
        raiz = math.sqrt(soma)
        print(f"Raiz quadrada da soma: {raiz}")
except ValueError:
    print("Entrada inválida.")