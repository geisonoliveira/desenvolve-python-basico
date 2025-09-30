valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas: #laço for vai percorrer a lista notas disponíveis
    qtd = valor // nota #usando divisão inteira para saber quantas notas de cada valor são necessárias
    print(f"{qtd} nota(s) de R${nota},00") #imprime a quantidade de notas necessárias
    valor -= qtd * nota #atualiza o valor restante subtraindo o valor das notas já contabilizadas