genero = input("Informe seu gênero (M ou F): ").upper()
idade = int(input("Informe sua idade: "))
tempo_servico = int(input("Informe seu tempo de serviço (em anos): "))

aposenta = (
    (genero == "F" and idade > 60) or
    (genero == "M" and idade > 65) or
    (tempo_servico >= 30) or
    (idade >= 60 and tempo_servico >= 25)
)

print(aposenta)