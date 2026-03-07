number = int(input("Verificador de número PAR: "))
while number != 0:
    if number % 2 == 0: 
        print("PAR")
    else:
        print("IMPAR")
    number = int(input())
    