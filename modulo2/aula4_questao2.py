fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))
celsius = int((fahrenheit - 32) * (5/9)) #usando int() já se converte para inteiro o valor gerado

print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius")