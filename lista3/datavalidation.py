# Exerc 3
print(" ============ Algoritmo de Validação de Dados ============ ")

while True:
    nota = float(input("Informe uma nota(0-10): "))
    if nota >= 0 and nota <= 10: break
    else: print("Forneça um valor válido! ")