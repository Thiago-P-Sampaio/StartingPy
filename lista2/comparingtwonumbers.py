#Exerc 4
print("============= Algoritmo que compara dois números ============= ")
num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe um número inteiro: "))


if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num1 < num2:
    print(f"{num2} é maior que {num1}")
else:
    print(f"{num1} é igual a {num2}")

