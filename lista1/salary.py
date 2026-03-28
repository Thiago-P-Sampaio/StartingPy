#Exercício 2.5

commission = (15/100)
salary = 800

sold_price = float(input("Valor correspondente das vendas: " )) 
salary += (sold_price * commission)
print(f"Salário do vendedor: R${salary}, com 800 reais fixos + {sold_price*commission} das vendas (15%)")
