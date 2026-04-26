#Exerc 5
print(" ============ Algoritmo de Média das idades ============ ")
idade = 0
media = 0
quant = 0
while idade != 999:
    idade = int(input("Informe a idade: "))
    if idade != 999: 
        quant += 1
        media += idade
else: 
    media /= quant
    print(f"{quant} pessoas foram registradas e a média foi de: {media:.2f}")