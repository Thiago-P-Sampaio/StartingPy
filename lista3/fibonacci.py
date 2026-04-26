# Exerc 6
print(" ============ Algoritmo de sequência de Fibonacci ============ ")
fibonacci = []
termos = int(input("Quantos termo de Fibonacci o usuário deseja que apareça: "))
i = 0
while i < termos:
    if(i == 0 or i == 1):  ## Adiciona os dois primeiros termos:  1 e 1
        fibonacci.append(1)
    else: 
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    i += 1 

for num in fibonacci:
    print(num)