#Exerc 10
print("============= Algoritmo que reajusta salário com base em vendas ============= ")
salario = 1200

vendas = int(input("Quantos sistemas o funcionário vendeu neste mês? "))

if vendas > 10:
    salario += vendas*80
    print(f"O funcionário recebeu um bônus de R${vendas*80:.2f}, e irá receber R${salario:.2f}")
else:
    salario += vendas*50
    print(f"O funcionário recebeu um bônus de R${vendas*50:.2f}, e irá receber R${salario:.2f}")