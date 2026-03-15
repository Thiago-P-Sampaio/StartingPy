soma = 0
quant = 0
while True:
    try:
        num = int(input("Digite um número(0 para sair): "))
        if num == 0:
            media = soma / quant
            print("A média é: ", media, "\n", "Quantidade: ", quant)
            break
        else: 
            soma += num
            quant += 1
        print("Soma: ", soma)

    except ValueError: 
        print("Informe um valor válido")