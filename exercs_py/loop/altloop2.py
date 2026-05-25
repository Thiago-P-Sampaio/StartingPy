primeira = []
segunda = []

while True:
    valor = int(input("Digite um valor para a primeira lista (0 para terminar): "))

    if valor == 0:
        break

    primeira.append(valor)

while True:
    valor = int(input("Digite um valor para a segunda lista (0 para terminar): "))

    if valor == 0:
        break

    segunda.append(valor)

terceira = []

duas_listas = primeira[:]

# duas_listas.extend(segunda)

for x in range(len(segunda)):
    duas_listas.append(segunda[x])

for x in range(len(duas_listas)):
    y = 0

    for y in range(len(terceira)):
        if duas_listas[x] == terceira[y]:
            break

        y = y + 1

    if y == len(terceira):
        terceira.append(duas_listas[x])

    x = x + 1

print("Conteúdo da terceira lista:", terceira)