#Exercício 2.3
weight1 = 2
weight2 = 3
weight3 = 5

print("Algoritmo que calcula a média ponderada")
test1 = float(input("Informe o valor da primeira prova:"))
test2 = float(input("Informe o valor da segunda prova:"))
test3 = float(input("Informe o valor da terceira prova:"))

final_average = ((test1 * weight1) + (test2 * weight2) + (test3 * weight3)) / (weight1 + weight2 + weight3)
print(f"Valor da nota final: {final_average}")