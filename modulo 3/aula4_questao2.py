avaliacao = int(input("Informe a avaliação do filme (1 a 5): "))
if avaliacao == 0 or avaliacao <0 or avaliacao >5:
    print("Avaliação inválida.")
elif avaliacao == 5:
    print("Excelente!.")
elif avaliacao == 4:
    print("Muito bom!.")
elif avaliacao == 3:
    print("Bom.")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim.")
