n = int(input("Digite o número de respondentes: "))
soma = 0

for i in range(n):
    idade = int(input(f"Digite a idade do respondente {i+1}: "))
    soma += idade

media = soma / n
print(f"A média das idades é: {media}")