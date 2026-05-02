print(" ============ Algoritmo de Caixa Eletrônico' ============ ")
num = int(input("Informe um valor(inteiro) a ser sacado: "))

subtracao_valores = [ 50, 20, 1]
cedulas = {}
i = 0
valor = 0

while i < 3:
    if num >= subtracao_valores[i]:
        num -= subtracao_valores[i]
        valor += 1
    else:
        cedulas[f"R${subtracao_valores[i]}"] = valor
        i +=1
        valor = 0

print("="*40)
for chave, valor in cedulas.items():
    print(f"{chave} = {valor}")