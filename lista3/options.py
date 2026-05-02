print("="*40 + "Algoritmo de Menu" + "="*40)

num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))

while True:

    opcao = int(input("Informe uma das opções a seguir: \n 1. Somar \n 2. Multiplicar \n 3. Maior valor \n 4. Novos números \n 5. Sair do programa \n resposta: "))
    match opcao:
        case 1: 
            soma = num1 + num2
            print(f"A soma: {num1} + {num2} = {soma}")
        case 2:
            mult = num1 * num2
            print(f"A soma: {num1} * {num2} = {mult}")
        case 3:
            print(f"O maior valor é {num1 if num1 > num2 else num2}")
        case 4:
            num1 = float(input("Informe um número: "))
            num2 = float(input("Informe outro número: "))
        case 5:
            break
        case _:
            break

print("="*40 + "Fim do programa" + "="*40)