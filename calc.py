print("Calculadora simples em python")

x = 1
while x  <= 100:
    n1 = int(input("Escolha um número: "))
    operacao = int(input("Escolha a operação: \n 1. +  \n 2. -  \n 3. /  \n 4. *  "))
    n2 = int(input("Escolha outro número: "))
    match operacao:
        case 1: 
            print("Resultado = ", n1 + n2)
        case 2: 
            print("Resultado = ", n1 - n2)
        case 3: 
            print("Resultado = ", n1 / n2)
        case 4: 
            print("Resultado = ", n1 * n2)

    x +=1

print("Fim")

