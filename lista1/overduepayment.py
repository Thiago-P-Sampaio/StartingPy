# Exercício 2.9

print("Algoritmo que realiza o cálculo de prestação em atraso")

while True:
    try:
        valor = float(input("Valor da prestação:    \n "))
        taxa = float(input("Taxa de juros imposto pelo banco: \n"))
        tempo = float(input("Dias em atraso: \n"))

        prestacao = valor + (valor * (taxa/100) * tempo)
        
        print(f"O valo da prestação, irá ficar R${prestacao}")
        break

    except ValueError:
        print("Informe um valor válido")
