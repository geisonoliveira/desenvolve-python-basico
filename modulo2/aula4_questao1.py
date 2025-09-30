comprimento = int(input("Digite o comprimento do terreno "))
largura =  int(input("Digite a largura do terreno "))
preco_m2 = float(input("Digite o preço por m2 do terreno "))

area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2

print(f"O terreno possui {area_m2}m2 e custa R$ {preco_total:.2f}") #formatando a string com .2f permite usar 2 casas decimais
