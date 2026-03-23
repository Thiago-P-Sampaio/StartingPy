#Exercício 2.4
balance = 500
while True:
    try:
        check = float(input("Valor do cheque a ser descontando R$"))
        if check < 0: break
        balance -=  check
        print(f"Saldo em conta bancária: R${balance}")
        break
    except ValueError:
        print("Informe um valor válido")