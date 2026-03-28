#Exercício 2.7

print("Algoritmo que calcula salário liquído")
while True:
    try:
        name = input("Informe o nome do funcionário(a):")
        salary = float(input(f"Olá {name}, Informe o seu rendimento bruto:  "))
        inss = 9/100 #desconto da previdência

        inss *= salary
        if salary > 0: 
            salary -= inss 
            break
        elif salary < 0: print("Insira um valor válido!")
        
    except ValueError:
        print("Informe valores válidos")


print(f"O salário líquido do funcionário(a) {name} é R${salary}, com o desconto de R$: {inss} da providência ")

