#Exerc 7
print("============= Algoritmo de Cálculadora ============= ")

while True:
    try:
        num1 = float(input("Informe um valor numérico: "))
        num2 = float(input("Informe outro valor numérico: "))


        operacao = int(input("Informe a operação desejada: \n 1. Soma \n  2. Subtração \n 3. Divisão \n 4. Multiplicação \n"))
        match operacao:
            case 1:
                soma = num1 + num2
                print(f"{num1} + {num2} = {soma}")
            case 2:
                sub = num1 - num2
                print(f"{num1} - {num2} = {sub}")
            case 3:
                div = num1 / num2
                print(f"{num1} / {num2} = {div}")
            case 4:
                mult = num1 * num2
                print(f"{num1} * {num2} = {mult}")
            case _:
                print("Opção inválida")
    
    except ValueError:
        print("Informe o valor correspondente ")