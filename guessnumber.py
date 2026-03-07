import random
print(" ================ Adivinhe o Número ==================")
print("1 - 20, você possui 10 tentativas! \n")
number = random.randint(1,20)
attemps = 1
while attemps <= 10:
    x = int(input("Informe um valor: "))
    if x == number:
        print("Você acertou \n Tentativas: ", attemps)
        break
    if attemps == 10:
        print("Você perdeu! \n O número era:", number)
    else:
        estimate = "Valor alto" if x > number else "Valor baixo"
        print(estimate)
        attemps += 1
        