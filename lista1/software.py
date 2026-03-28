#Exercício 2.6:

salary = 500
print("Algoritmo que calcula o salário de vendedor")
while True:
    try:
        software_sales = int(input("Informe quantos sistemas foram vendidos pelo vendedor de software: "))
        salary += 50*software_sales 
        break
    except ValueError:
        print("Informe um valor válido")

print(f"O Salário do vendedor é de R${salary}. Ele obteve {software_sales} vendas")

