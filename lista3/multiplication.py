# Exerc 4
print(" ============ Algoritmo de Tabuada ============ ")
resposta = "sim"
while resposta == "sim" or resposta == "s":
    num = int(input("Informe um número para a Tabuada: "))
    controlador = 1
    while controlador <= 10:
        print(f"{num} x {controlador} = {num * controlador}")
        controlador += 1
    else:
        resposta = input("Deseja ver a tabuada de outro número? 'S' ou 'N' ").lower()
else: 
    print("Fim do programa")