#Exerc 6
print("============= Algoritmo que classifica Triângulos ============= ")

while True:
    try:
        lado1 = int(input("Informe um valor para o primeiro lado: "))
        lado2 = int(input("Informe um valor para o segundo lado: "))
        lado3 = int(input("Informe um valor para o terceiro lado: "))

        if lado1 == lado2 and lado1 == lado3:
            print(f"O triângulo: {lado1}, {lado2}, {lado3} é Equilátero")
            break
        elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            print(f"O triângulo: {lado1}, {lado2}, {lado3} é Escaleno")
            break
        else: 
            print(f"O triângulo: {lado1}, {lado2}, {lado3} é Isósceles")
            break
    except ValueError:
        print("Informe um valor válido para o campo correspondente!")