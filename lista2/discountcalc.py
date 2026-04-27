#Exerc 5
print("============= Algoritmo que calcula desconto INSS ============= ")
while True:
    try:
        salario = float(input("Informe o salário bruto: "))
        if salario > 2000:
            salario -= salario * (11/100)
            print(f"Foi aplicado um desconto de 11% em cima do salário bruto, resultando em R${salario:.2f}")
            break
        else:
            salario -= salario * (9/100)
            print(f"Foi aplicado um desconto de 9% em cima do salário bruto, resultando em R${salario:.2f}")
            break
    except ValueError:
        print("Informe um valor válido ao campo correspondente")